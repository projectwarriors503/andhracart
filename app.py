from flask import Flask, jsonify
from config import get_config
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*")  # Allow frontend access

@app.route("/config", methods=["GET"])
def send_config_to_frontend():
    config = get_config()
    return jsonify({
        "firebase": config["firebase"],
        "supabase": {
            "url": config["supabase"]["url"],
            # DO NOT return service_role key here
        }
    })

@app.route("/admin-supabase-key", methods=["GET"])
def internal_supabase_key():  # example: protected route
    config = get_config()
    return jsonify({"key": config["supabase"]["key"]})  # expose only in secure/internal use

if __name__ == "__main__":
    app.run(debug=True)
