from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="UP")

@app.route("/order", methods=["POST"])
def create_order():
    data = request.json
    return jsonify({
        "message": "Order created",
        "order": data
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
