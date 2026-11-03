# 📝 User Information Collector

A simple Python command-line application that collects user information, validates inputs, calculates basic statistics, displays a formatted summary, and saves the information into a text file.

## 🚀 Features

- Collect user information:
  - First Name
  - Last Name
  - Age
  - Email
  - Phone Number
  - City
- Calculate birth year based on age.
- Validate age (must be positive).
- Validate email (must contain @).
- Validate phone number (10-digit Indian mobile number).
- Collect programming experience details.
- Calculate average programming languages per year of experience.
- Determine programming experience level.
- Display colored terminal output using Colorama.
- Save collected information into a text file.

## 🛠️ Technologies Used

- Python 3
- Colorama
- File Handling
- Conditional Statements
- Loops
- Exception Handling
- String Formatting

## 📦 Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the project directory

```bash
cd basic
```

### 3. Install dependencies

```bash
pip install colorama
```

## ▶️ Run the Application

```bash
python user_info_collector.py
```

## 📁 Project Structure

```text
User-Information-Collector/
│
├── user_info_collector.py
├── user_info.txt
└── README.md
```

## 💻 Sample Output

```text
=============================================
          USER INFORMATION SUMMARY
=============================================

Name: Nimmi Sunder
Age: 33
Birth Year: 1993
Email: nimmi@example.com
Phone: 9876543210
City: Kollam

PROGRAMMING EXPERIENCE

Languages Known: 3
Favorite Language: Python
Years of Experience: 9
Average Languages/Year: 0.33
Experience Level: Advanced

Student Status: Yes

=============================================
Information saved successfully!
=============================================
```

## 📚 Learning Objectives

This project was developed to practise fundamental Python programming concepts:

1. Variables and Data Types
2. User Input and Output
3. Type Conversion
4. Arithmetic Operators
5. Comparison and Logical Operators
6. Conditional Statements (`if`, `elif`, `else`)
7. Loops (`while`)
8. Input Validation
9. Exception Handling (`try`, `except`)
10. External Libraries (`Colorama`)
11. File Handling (`open`, `write`, `append`)
12. String Formatting (f-strings)

## 🔮 Future Improvements

- Add stronger email validation.
- Support international phone numbers.
- Save user information in CSV or JSON format.
- Add a feature to retrieve previously saved user information.
- Introduce a database using SQLite.
- Build a graphical user interface.

## 👩‍💻 Author

Developed as a Python learning project.

---

**Learning Python one project at a time! 🚀**
