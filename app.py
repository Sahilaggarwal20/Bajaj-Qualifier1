from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# GET method endpoint
@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    operation_code = {"operation_code": 1}
    return render_template("index.html", operation_code=operation_code)

# POST method endpoint
@app.route('/bfhl', methods=['POST'])
def process_data():
    data = request.json.get("data", [])
    print(data)
    user_id = "john_doe_17091999"
    email = "john@xyz.com"
    roll_number = "ABCD123"

    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    highest_lowercase_alphabet = max([ch for ch in data if ch.islower()], default=None)

    response = {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
    }

    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)
