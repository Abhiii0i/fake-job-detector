
import streamlit as st
import joblib

# Load the trained model
model = joblib.load("fake_job_detection_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Fake Job Detector",
    page_icon="🔎",
    layout="centered"
)

# App heading
st.title("🔎 Fake Job Posting Detector")
st.write(
    "Check whether a job advertisement may be fraudulent "
    "using a machine-learning model."
)

st.warning(
    "This tool provides an estimate, not a guarantee. "
    "Always verify employers independently."
)

# User input
job_title = st.text_input("Job Title")
company_profile = st.text_area("Company Profile")
description = st.text_area("Job Description")

# Prediction button
if st.button("Check Job Posting"):
    if not job_title.strip() and not company_profile.strip() and not description.strip():
        st.error("Please enter at least some job information.")
    else:
        # Combine text in the same order used during training
        job_text = (
            job_title + " " +
            company_profile + " " +
            description
        )

        prediction = model.predict([job_text])[0]

        if prediction == 1:
            st.error("⚠️ Potentially Fake Job Posting")
        else:
            st.success("✅ Likely Genuine Job Posting")

        st.caption(
            "This prediction is not proof of fraud or authenticity."
        )
