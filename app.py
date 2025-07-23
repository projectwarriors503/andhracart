import os
from flask import Flask, jsonify
from flask_cors import CORS
from config import get_config

app = Flask(__name__)
CORS(app, origins=["https://andhracart.netlify.app"])  # ✅ No indentation error

@app.route("/config", methods=["GET"])
def send_config_to_frontend():
    config = get_config()
    return jsonify({
        "firebase": config["firebase"],
        "supabase": {
            "url": config["supabase"]["url"],
            "anonKey": os.getenv("SUPABASE_ANON_KEY")  # ✅ Add this line
        }
    })


@app.route("/admin-supabase-key", methods=["GET"])
def internal_supabase_key():
    config = get_config()
    return jsonify({"key": config["supabase"]["key"]})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
