import numpy as np
import librosa
import streamlit as st
import io
import torch
from speechbrain.inference.speaker import EncoderClassifier

@st.cache_resource
def load_voice_encoder():
    return EncoderClassifier.from_hparams(
        source="speechbrain/spkrec-ecapa-voxceleb",
        savedir="pretrained_models/spkrec-ecapa-voxceleb"
    )

def get_voice_embeddings(audio_bytes):
    try:
        encoder = load_voice_encoder()
        audio, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)
        
        # SpeechBrain expects a tensor [batch, time]
        wav = torch.tensor(audio, dtype=torch.float32).unsqueeze(0)
        with torch.no_grad():
            embedding = encoder.encode_batch(wav)
        
        # Convert to numpy and normalize for cosine similarity
        embedding_np = embedding.squeeze().cpu().numpy()
        norm = np.linalg.norm(embedding_np)
        if norm > 0:
            embedding_np = embedding_np / norm
        
        return embedding_np.tolist()
    except Exception as e:
        st.error(f"Voice processing error: {e}")
        return None
    
def identify_speaker(new_embedding, candidate_dict, threshold=0.75):
    if new_embedding is None or not candidate_dict:
        return None, 0
    
    best_sid= None
    best_score = -1

    for s_id, stored_embeddings in candidate_dict.items():
        if stored_embeddings:
            stored_embeddings = np.array(stored_embeddings)
            similarity = np.dot(new_embedding, stored_embeddings)
            if similarity > best_score:
                best_score = similarity
                best_sid = s_id
    
    if best_score >= threshold:
        return best_sid, best_score
    
    return None, best_score

def process_bulk_audio(audio_bytes, candidates_dict, threshold=0.75):
    try:
        encoder = load_voice_encoder()
        audio, sr = librosa.load(io.BytesIO(audio_bytes), sr = 16000)
        segments = librosa.effects.split(audio, top_db = 20)

        identified_results = {}
        
        for start_time, end_time in segments:
            # Skip segments that are too short (less than 0.5 seconds)
            if (end_time - start_time) < sr * 0.5:
                continue
            
            segment_audio = audio[start_time:end_time]
            wav = torch.tensor(segment_audio, dtype=torch.float32).unsqueeze(0)
            
            with torch.no_grad():
                embedding = encoder.encode_batch(wav)
            embedding_np = embedding.squeeze().cpu().numpy()
            
            # Normalize embedding
            norm = np.linalg.norm(embedding_np)
            if norm > 0:
                embedding_np = embedding_np / norm
            
            sid, score = identify_speaker(embedding_np, candidates_dict, threshold)
            if sid:
                if sid not in identified_results or score > identified_results[sid]:
                    identified_results[sid] = score

        return identified_results
    except Exception as e:
        st.error(f"Voice processing error: {e}")
        return {}
                
            