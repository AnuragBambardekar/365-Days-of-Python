"""
pip install streamlit
streamlit run .\calculator.py
"""

import streamlit as st

# Define the grade to GPA mapping
grade_to_gpa = {
    'A': 4.0,
    'B': 3.0,
    'C': 2.0,
    'D': 1.0,
    'F': 0.0
}

st.title("GPA Calculator (4.0 Scale)")

# Create an input field for the number of courses
num_courses = st.number_input("Enter the number of courses:", min_value=1, value=1, step=1)

grades = []

# Create input fields for each course's grade
for i in range(num_courses):
    grade = st.selectbox(f"Select the grade for Course {i+1}:", list(grade_to_gpa.keys()))
    grades.append(grade)

# Calculate & Display the GPA
total_points = sum(grade_to_gpa[grade] for grade in grades)
gpa = total_points / num_courses

st.write(f"Your GPA on a 4.0 scale is: {gpa:.2f}")
