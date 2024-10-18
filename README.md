# Password Strength Tool

## 📋 Overview

The **Password Strength Tool** is a web-based application designed to help users **generate** strong passwords and **analyze** the strength of existing ones. This tool provides both a **Random Password Generator** and a **Password Strength Analyzer**, making it easier to create secure passwords while ensuring they meet security standards.

### 🔑 Features

- **Random Password Generator**: Easily generate secure passwords with customizable length.
- **Password Strength Analyzer**: Real-time feedback on the strength of passwords based on length, variety of characters, and the inclusion of uppercase, lowercase, numbers, and special characters.
- **User-Friendly Design**: The password generator and strength analyzer are placed side by side for an intuitive, easy-to-use interface.
- **Responsive Layout**: Built with **CSS Flexbox**, the tool adapts seamlessly to different screen sizes and devices.

## 🚀 How to Run the Project

Follow these steps to get the project up and running locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/password-strength-tool.git
Navigate to the Project Directory:

bash
Copy code
cd password-strength-tool
Install Required Python Packages: Make sure you have Flask installed.

bash
Copy code
pip install flask
Run the Flask App:

bash
Copy code
python app.py
Open in Your Browser: Navigate to the following URL in your browser to use the tool:

arduino
Copy code
http://127.0.0.1:5000/
📁 Project Structure
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
🛠️ Technologies Used
Frontend: HTML, CSS (Flexbox)
Backend: Flask (Python)
💻 Usage Instructions
Generate a Random Password:

Use the slider to select the desired password length.
Click the "Generate Password" button to generate a random password.
Copy the password using the "Copy to Clipboard" button for easy access.
Analyze a Password:

Type or paste a password into the Password Strength Analyzer input field.
Receive instant feedback on the password strength, categorized as Weak, Medium, Strong, or Super Strong.