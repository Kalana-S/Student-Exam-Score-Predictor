import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(
    page_title="Student Exam Score Predictor",
    layout="centered"
)

@st.cache_resource
def load_model():
    with open("model/lgbm_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

gender_map = {"other": 0, "male": 1, "female": 2}
course_map = {
    "diploma": 0, "ba": 1, "b.sc": 2, "b.com": 3,
    "bba": 4, "bca": 5, "b.tech": 6
}
internet_access_map = {"no": 0, "yes": 1}
sleep_quality_map = {"poor": 0, "average": 1, "good": 2}
study_method_map = {
    "self-study": 0, "group study": 1,
    "online videos": 2, "mixed": 3, "coaching": 4
}
facility_rating_map = {"low": 0, "medium": 1, "high": 2}
exam_difficulty_map = {"easy": 0, "moderate": 1, "hard": 2}

st.markdown(
    """
    <h1 style="text-align:center;">🎓 Student Exam Score Predictor</h1>
    <p style="text-align:center; color:gray;">
        Enter student details to predict the expected exam score
    </p>
    """,
    unsafe_allow_html=True
)

st.sidebar.header("📌 Student Information")

age = st.sidebar.number_input("Age", 16, 26, 20)
gender = st.sidebar.selectbox("Gender", list(gender_map.keys()))
course = st.sidebar.selectbox("Course", list(course_map.keys()))
study_hours = st.sidebar.number_input("Daily Study Hours", 0.0, 10.0, 4.0, 0.1)
class_attendance = st.sidebar.number_input("Class Attendance (%)", 40.0, 100.0, 80.0)
internet_access = st.sidebar.selectbox("Internet Access", list(internet_access_map.keys()))
sleep_hours = st.sidebar.number_input("Sleep Hours", 4.0, 10.0, 7.0, 0.1)
sleep_quality = st.sidebar.selectbox("Sleep Quality", list(sleep_quality_map.keys()))
study_method = st.sidebar.selectbox("Study Method", list(study_method_map.keys()))
facility_rating = st.sidebar.selectbox("Facility Rating", list(facility_rating_map.keys()))
exam_difficulty = st.sidebar.selectbox("Exam Difficulty", list(exam_difficulty_map.keys()))

input_data = {
    "age": age,
    "gender": gender_map[gender],
    "course": course_map[course],
    "study_hours": study_hours,
    "class_attendance": class_attendance,
    "internet_access": internet_access_map[internet_access],
    "sleep_hours": sleep_hours,
    "sleep_quality": sleep_quality_map[sleep_quality],
    "study_method": study_method_map[study_method],
    "facility_rating": facility_rating_map[facility_rating],
    "exam_difficulty": exam_difficulty_map[exam_difficulty],
}

input_df = pd.DataFrame([input_data])
input_df = input_df[model.feature_names_in_]

if st.button("🔮 Predict Exam Score"):
    prediction = model.predict(input_df)[0]
    prediction = np.clip(prediction, 0, 100)

    st.success(f"📊 **Predicted Exam Score: {prediction:.2f} / 100**")

    st.markdown("### 🔍 Model Input Preview")
    st.dataframe(input_df)
