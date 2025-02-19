from flask import Flask, render_template, request, jsonify
import csv

app = Flask(__name__)

# Function to check if user exists in either CSV file
def is_real_user(user_id, user_name):
    files = ['fakeusers.csv', 'realusers.csv']  # List of CSV files

    for file in files:
        with open(file, mode='r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['id'] == user_id and row['name'] == user_name:
                    return True  # If found in any file, return True
    return False

# Home route (renders the login page)
@app.route('/')
def home():
    return render_template("index.html")

# Route to handle form submission
@app.route('/predict', methods=["POST"])
def predict():
    user_id = request.form.get('id')
    user_name = request.form.get('name')

    print(f"Received user_id: {user_id}, user_name: {user_name}")  # Debugging

    # Check if user exists in either CSV
    if is_real_user(user_id, user_name):
        result = "Real"
    else:
        result = "Fake"

    return jsonify({"classification": result})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
