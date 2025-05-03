import sys
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # Get parameter from command-line or use default
    message = sys.argv[1] if len(sys.argv) > 1 else "Default Message"
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
