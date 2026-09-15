from src.database.config import supabase
import bcrypt

def hash_pass(password):
    return bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())

def check_teacher(username):
    response = supabase.table("teachers").select("username").eq("username",username).execute()
    return len(response.data) > 0

def create_teacher(username,name,password):
    data = {
        "username":username,
        "name":name,
        "password_hash":hash_pass(password)
    }

    response = supabase.table("teachers").insert(data).execute()
    return response

def teacher_login(username, password):
    response = supabase.table("teachers").select("*").eq("username",username).execute()
    if response.data:
        teacher = response.data[0]
        if bcrypt.checkpw(password.encode('utf-8'), teacher["password_hash"]):
            return teacher
    return None