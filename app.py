from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# Function to check password strength
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."
    if not re.search("[a-z]", password) or not re.search("[A-Z]", password):
        return "Weak: Password should contain both uppercase and lowercase characters."
    if not re.search("[0-9]", password):
        return "Weak: Password should contain at least one number."
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Password should contain at least one special character."
    return "Strong: Your password is strong!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check-password', methods=['POST'])
def check_password():
    data = request.get_json()
    password = data.get('password', '')
    result = check_password_strength(password)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
