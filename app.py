from flask import Flask, request, jsonify

app = Flask(__name__)

# Global variable to store the seed value (default = 0)
seed_value = 0

@app.route("/", methods=["POST"])
def update_seed():
    global seed_value
    try:
        data = request.get_json()
        if "num" in data and isinstance(data["num"], int):
            seed_value = data["num"]
            return jsonify({"message": "Seed updated", "seed": seed_value}), 200
        else:
            return jsonify({"error": "Invalid JSON body. Must include {'num': integer}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def get_seed():
    return str(seed_value), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)  # Runs on port 5000 (adjustable)
