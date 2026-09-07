# Advanced BMI Calculator

## OASIS INFOBYTE - Python Programming Internship

### Task 2: BMI Calculator

An advanced desktop-based BMI Calculator developed using Python and Tkinter.

The application calculates Body Mass Index (BMI), classifies the result into different BMI categories, stores historical records using SQLite, supports multiple users, and provides BMI trend visualization using Matplotlib.

---

## Features

- User-friendly graphical interface using Tkinter
- BMI calculation using weight and height
- Color-coded BMI results
- BMI category classification
- Multiple-user support
- SQLite database for historical records
- BMI history table
- User-based history filtering
- BMI trend visualization
- Delete selected history records
- Input validation
- Database error handling
- Clear input functionality
- Professional desktop interface

---

## BMI Categories

| BMI Range | Category |
|-----------|----------|
| Below 18.5 | Underweight |
| 18.5 - 24.9 | Normal |
| 25.0 - 29.9 | Overweight |
| 30.0 and above | Obese |

---

## Technologies Used

- Python
- Tkinter
- SQLite3
- Matplotlib

---

## Project Structure

```text
Python-Task2-BMICalculator/
│
├── app.py
├── bmi_calculator.py
├── database.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── screenshots/
│   ├── bmi_calculator_home.png
│   ├── bmi_normal_result.png
│   ├── bmi_history.png
│   └── bmi_trend.png
│
└── data/
    └── .gitkeep