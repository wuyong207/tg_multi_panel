from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/test")
def test():
    return jsonify({"status": "Flask 服务运行成功"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

