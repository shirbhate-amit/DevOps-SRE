import sys
from flask import Flask

app = Flask(__name__)

# Capture the command-line argument
param = sys.argv[1] if len(sys.argv) > 1 else "default"

@app.route('/')
def hello():
    return f"Hello, Jenkins CI/CD! Parameter: {param}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
