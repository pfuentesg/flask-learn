from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "holi"

app.run(port=3030)

