from flask import Flask, request, jsonify

app = Flask(__name__)

VALID_USERNAME = "admin"
VALID_PASSWORD = "secret123"
MAX_ATTEMPTS = 5

attempts = {}

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username not in attempts:
        attempts[username] = 0

    if attempts[username] >= MAX_ATTEMPTS:
        return jsonify({"message": "Account locked"}), 403

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        return jsonify({"message": "Login successful"}), 200
    else:
        attempts[username] += 1
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(debug=True)
