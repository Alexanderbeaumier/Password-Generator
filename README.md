# Password-Generator

Overview
The Password Strength Tool is a web-based application that combines a Random Password Generator and a Password Strength Analyzer. The tool helps users generate secure passwords and analyze the strength of passwords based on common security criteria.

Features
Random Password Generator: Allows users to generate strong, random passwords with customizable length.
Password Strength Analyzer: Analyzes the strength of user-provided passwords based on length, character variety, and the inclusion of uppercase, lowercase, numbers, and special characters.
Side-by-Side Layout: The password generator and strength analyzer are displayed side by side for convenience.
Responsive Design: The app adjusts for different screen sizes and resolutions using CSS Flexbox.
Demo

How to Run the Project
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/password-strength-tool.git
Navigate to the project directory:

bash
Copy code
cd password-strength-tool
Install the necessary Python packages:

bash
Copy code
pip install flask
Run the Flask app:

bash
Copy code
python app.py
Open a browser and go to:

arduino
Copy code
http://127.0.0.1:5000/
Project Structure
plaintext
Copy code
password-strength-tool/
│
├── app.py               # Flask backend to run the app
├── start_app.py         # Python script to start the Flask app
├── templates/
│   └── index.html       # Frontend HTML file for the app
└── static/
    └── styles.css       # CSS for styling the app
Technologies Used
Frontend: HTML, CSS (Flexbox)
Backend: Flask (Python)
Usage
Generate a Random Password: Use the slider to select the password length, then click "Generate Password" to create a random password.
Analyze a Password: Type or paste a password in the Password Strength Analyzer field, and the app will analyze the strength of the password in real-time.