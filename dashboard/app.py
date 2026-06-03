import streamlit as st
import requests

st.title("AI Learning Recommendation System")

student_id = st.number_input(
    "Enter Student ID",
    min_value=1,
    value=1,
    step=1
)

if st.button("Get Recommendations"):
    try:
        response = requests.get(
            f"http://127.0.0.1:5000/recommend/{student_id}"
        )

        data = response.json()

        st.success(f"Recommendations for Student {student_id}")

        for course in data["recommended_courses"]:
            st.markdown(f"- **{course}**")

    except Exception as e:
        st.error(f"Error: {e}")