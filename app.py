import os
from flask import Flask

app = Flask(__name__)

ENVIRONMENT = os.getenv("APP_ENV", "dev")
PORT = int(os.getenv("APP_PORT", 4000))

@app.route("/")
def home():
    if ENVIRONMENT == "live":
        return "<h1>Welcome to Live Auto-Deployed</h1><p>Environment: Production</p>"
    else:
        return "<h1>Welcome to the My Dev Environment</h1><p>The app is running on Port 4000</p>"

if __name__ == "__main__":
    is_debug = True if ENVIRONMENT == "dev" else False
    app.run(host="0.0.0.0", port=PORT, debug=is_debug)
