"""
Mumbai University - CGPI Calculator
The CGPI in Mumbai University is calculated as,

CGPI = ∑ (𝐶𝑖 ∗ 𝐺𝑖) / ∑ 𝐶𝑖

where, 𝐶𝑖 are the credits earned in each course, and 𝐺𝑖 are grade points in these courses.

SGPI = Semester Grade Point Index
CGPI = Cumulative Grade Point Index
"""

import streamlit as st

st.title("CGPI and Percentage Calculator with Grade")

# Create an empty list to store SGPIs
sgpi_list = []

# Input for the number of semesters
num_semesters = st.number_input("Enter the number of semesters:", min_value=1, value=1, step=1)

# Input fields for SGPIs
for i in range(num_semesters):
    st.header(f"Semester {i + 1}")
    sgpi_text = st.text_input(f"SGPI for Semester {i + 1}:", f"0.00", key=f"sgpi_{i}")
    sgpi = float(sgpi_text)
    sgpi_list.append(sgpi)

# Calculate the CGPI
total_sgpi = sum(sgpi_list)
cgpi = total_sgpi / num_semesters if num_semesters > 0 else 0.0

# Convert CGPI to Percentage
percentage = 7.1 * cgpi + 11

# Determine the grade and performance
grade = ""
performance = ""
if percentage >= 80:
    grade = "O"
    performance = "Outstanding"
elif percentage >= 75:
    grade = "A"
    performance = "Excellent"
elif percentage >= 70:
    grade = "B"
    performance = "Very Good"
elif percentage >= 60:
    grade = "C"
    performance = "Good"
elif percentage >= 50:
    grade = "D"
    performance = "Fair"
elif percentage >= 45:
    grade = "E"
    performance = "Average"
elif percentage >= 40:
    grade = "P"
    performance = "Pass"
else:
    grade = "F"
    performance = "Fail"

# Display CGPI, Percentage, Grade, and Performance
st.markdown(f'<p style="color: green; font-size: 24px;">Your CGPI is: {cgpi:.2f}</p>', unsafe_allow_html=True)
st.markdown(f'<p style="color: blue; font-size: 24px;">Your Percentage is: {percentage:.2f}%</p>', unsafe_allow_html=True)
st.write(f'<p style="color: blue; font-size: 24px;">Grade: {grade}</p>', unsafe_allow_html=True)
st.write(f'<p style="color: blue; font-size: 24px;">Performance: {performance}</p>', unsafe_allow_html=True)

# Optionally, you can display a list of SGPIs
if num_semesters > 0:
    st.subheader("SGPIs for Each Semester")
    for i in range(num_semesters):
        st.write(f"Semester {i + 1}: {sgpi_list[i]:.2f}")


