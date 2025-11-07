from flask import Flask, jsonify

app = Flask(__name__, static_folder="static", static_url_path="")

@app.get("/")
def home():
    return app.send_static_file("index.html")

@app.get("/api/hello")
def hello():
    return jsonify(message="Hello from Python Flask")

if __name__ == "__main__":
    app.run(port=5001, debug=True)

@app.get("/favicon.ico")
def favicon():
    return app.send_static_file("favicon.ico")
