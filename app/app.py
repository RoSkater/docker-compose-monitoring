from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask App Up and Running!"

@app.route("/metrics")
def metrics():
    return f"myapp_requests_total {random.randint(0, 100)}\n"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
