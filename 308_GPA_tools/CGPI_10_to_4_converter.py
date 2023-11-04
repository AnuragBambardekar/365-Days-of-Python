import streamlit as st

def convert_10_scale_to_4_scale(gpa_10_scale):
    return 4.0 * (gpa_10_scale / 10.0)

st.title("GPA Conversion (10-point to 4-point Scale)")

# Create an input field for the GPA on a 10-point scale
gpa_10_scale = st.number_input("Enter GPA on a 10-point scale:", min_value=0.0, max_value=10.0, value=0.0, step=0.1)

# Convert the GPA and display it
gpa_4_scale = convert_10_scale_to_4_scale(gpa_10_scale)
st.write(f"GPA on a 4-point scale: {gpa_4_scale:.2f}")
