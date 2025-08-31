from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def check_strength(password: str) -> dict:
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        "length": not length_error,
        "digit": not digit_error,
        "uppercase": not uppercase_error,
        "lowercase": not lowercase_error,
        "symbol": not symbol_error
    }

    score = sum(errors.values())
    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return {"score": score, "strength": strength, "checks": errors}

@app.route("/api/check", methods=["POST"])
def check_password():
    data = request.get_json()
    password = data.get("password", "")
    result = check_strength(password)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
