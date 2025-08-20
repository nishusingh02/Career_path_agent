import streamlit as st
import requests

st.title("Career Path Agent")

with st.form("employee_form"):
    name = st.text_input("Name")
    role = st.text_input("Role")
    department = st.text_input("Department")
    experience = st.number_input("Years of Experience", min_value=0)
    career_goal = st.text_input("Career Goal")
    performance_rating = st.slider("Performance Rating", 1.0, 5.0, 3.0)
    feedback = st.text_area("Feedback")
    submitted = st.form_submit_button("Get Recommendations")

if submitted:
    data = {
        "name": name,
        "role": role,
        "department": department,
        "experience": experience,
        "career_goal": career_goal,
        "performance_rating": performance_rating,
        "feedback": feedback
    }
    response = requests.post("http://localhost:5000/recommend", json=data)
    if response.ok:
        recs = response.json()
        st.subheader("Suggested Learning Paths")
        for lp in recs["learning_paths"]:
            st.write(lp)
        st.subheader("Job Rotation Options")
        for jr in recs["job_rotations"]:
            st.write(jr)
    else:
        st.error("Error fetching recommendations.")