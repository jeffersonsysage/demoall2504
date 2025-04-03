# app.py
from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 啟用 CORS

@app.route('/')
def index():
    return render_template('index.html')  # 會渲染我們的 HTML 頁面

@app.route('/api/greet')
def greet():
    return jsonify(message="Simple AKS Automated deployments ")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

