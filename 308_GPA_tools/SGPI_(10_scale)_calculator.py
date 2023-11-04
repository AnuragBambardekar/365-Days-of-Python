"""
SGPI = ∑ (𝐶𝑖 ∗ 𝐺𝑖) / ∑ 𝐶𝑖
where, 𝐶𝑖 are the credits earned in each course, and 𝐺𝑖 are grade points (out of 10) in these courses.
"""

import streamlit as st

st.title("SGPI Calculator (10.0 Scale)")

# Create empty lists to store subject details
subject_names = []
subject_codes = []
credits_earned = []
grade_points = []

# Input for the number of courses
num_courses = st.number_input("Enter the number of courses:", min_value=1, value=1, step=1)

# Input fields for subject details
for i in range(num_courses):
    st.header(f"Course {i+1}")
    subject_name = st.text_input(f"Subject Name {i+1}:", key=f"subject_name_{i}")
    subject_code = st.text_input(f"Subject Code {i+1}:", key=f"subject_code_{i}")
    credit = st.number_input(f"Credits Earned {i+1}:", min_value=0, step=1, key=f"credit_{i}")
    grade_point = st.number_input(f"Grade Points {i+1} (out of 10):", min_value=0.0, max_value=10.0, step=0.1, key=f"grade_point_{i}")
    
    subject_names.append(subject_name)
    subject_codes.append(subject_code)
    credits_earned.append(credit)
    grade_points.append(grade_point)

# Calculate the SGPI
total_credit_points = sum(credit * grade_point for credit, grade_point in zip(credits_earned, grade_points))
total_credits = sum(credits_earned)
# print(total_credit_points, total_credits)
sgpi = total_credit_points / total_credits if total_credits > 0 else 0.0

# Display SGPI
st.markdown(f'<p style="color: blue; font-size: 24px;">Your SGPI is: {sgpi:.2f}</p>', unsafe_allow_html=True)

# Optionally, you can display a table of subject details
if num_courses > 0:
    st.subheader("Subject Details")
    subject_data = {
        "Subject Name": subject_names,
        "Subject Code": subject_codes,
        "Credits Earned": credits_earned,
        "Grade Points": grade_points,
    }
    st.table(subject_data)

