import os
from dotenv import load_dotenv

load_dotenv()

def get_config():
    return {
        "firebase": {
            "apiKey": os.getenv("FIREBASE_API_KEY"),
            "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
            "projectId": os.getenv("FIREBASE_PROJECT_ID"),
            "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
            "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
            "appId": os.getenv("FIREBASE_APP_ID"),
            "measurementId": os.getenv("FIREBASE_MEASUREMENT_ID"),
        },
        "supabase": {
            "url": os.getenv("SUPABASE_URL"),
            "anonkey": os.getenv("SUPABASE_KEY")  # ⚠️ Only return this to backend logic
        }
    }
