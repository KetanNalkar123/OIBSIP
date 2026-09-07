"""
BMI Calculator Logic
OASIS INFOBYTE - Python Programming Internship
Task 2: Advanced BMI Calculator
"""


def calculate_bmi(weight_kg, height_cm):
    """
    Calculate BMI from weight in kilograms and height in centimeters.

    Returns:
        tuple: (bmi, category)
    """

    if weight_kg <= 0:
        raise ValueError("Weight must be greater than 0.")

    if height_cm <= 0:
        raise ValueError("Height must be greater than 0.")

    height_m = height_cm / 100

    bmi = weight_kg / (height_m ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return round(bmi, 2), category


def get_category_color(category):
    """
    Return a color for the BMI category.
    """

    colors = {
        "Underweight": "#3498DB",
        "Normal": "#27AE60",
        "Overweight": "#F39C12",
        "Obese": "#E74C3C"
    }

    return colors.get(category, "#34495E")