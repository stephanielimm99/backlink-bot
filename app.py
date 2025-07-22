from flask import Flask
from bot import run_bot

app = Flask(__name__)

@app.route('/run', methods=['POST'])
def trigger():
    run_bot()
    return "Bot dijalankan!", 200

if __name__ == "__main__":
    app.run(debug=True)
