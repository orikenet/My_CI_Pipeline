from flask import Flask
import os

app = Flask(__name__)

MESSAGE = os.getenv("MESSAGE", "Hello from Flask!")

@app.route("/")
def home():
    return {
        "message": MESSAGE
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
