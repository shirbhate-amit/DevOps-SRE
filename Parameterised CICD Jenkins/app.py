import sys
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    param = sys.argv[1] if len(sys.argv) > 1 else "default"
    return f"Hello from Jenkins! Received param: {param}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
