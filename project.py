import os
from flask import Flask
from flask_executor import Executor
app = Flask(__name__)

executor = Executor(app)

@app.route("/")
def hello():
    return "Working...!"

@app.route("/mrager")
def index():
    executor.submit(long_running_job)
    return "Projecting..."

def long_running_job():
    os.system("python mrager.py")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
