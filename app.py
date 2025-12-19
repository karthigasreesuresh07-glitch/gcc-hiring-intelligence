import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ------------------ CONFIG ------------------
st.set_page_config(
    page_title="GCC Hiring Intelligence Platform",
    page_icon="📊",
    layout="wide"
)

# ------------------ AI LOGIC ------------------
def match_score(jd, resume):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([jd, resume])
    score = cosine_similarity(vectors)[0][1]
    return round(score * 100, 2)

# ------------------ SIDEBAR ------------------
st.sidebar.title("GCC Hiring Platform")
st.sidebar.caption("AI-Driven Talent Intelligence")

menu = st.sidebar.radio(
    "Navigate",
    [
        "Executive Dashboard",
        "Talent Discovery",
        "Interview Evaluation",
        "Engagement & Risk",
        "Hiring Assistant"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "Prototype Focus:\n"
    "- Intelligence Layer\n"
    "- Decision Support\n"
    "- GCC Hiring Use-Cases"
)

# ------------------ DASHBOARD ------------------
if menu == "Executive Dashboard":
    st.title("Executive Hiring Dashboard")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Open Positions", "12")
    col2.metric("Active Candidates", "87")
    col3.metric("Avg Skill Match", "82%")
    col4.metric("Drop-Off Risk", "18%")

    st.markdown("---")

    st.subheader("Hiring Lifecycle Coverage")
    st.write(
        """
        ✔ Talent Discovery & Resume Screening  
        ✔ Interview Decision Intelligence  
        ✔ Post-Offer Engagement & Risk Prediction  
        ✔ Conversational Hiring Assistant  
        """
    )

    st.success(
        "This dashboard demonstrates how GCCs can convert hiring "
        "from a manual workflow into a predictive intelligence system."
    )

# ------------------ MODULE 1 ------------------
elif menu == "Talent Discovery":
    st.title("Talent Discovery & Resume Screening")

    st.caption("AI-based skill matching between Job Description and Resume")

    jd = st.text_area("Job Description", height=150)
    resume = st.text_area("Candidate Resume", height=150)

    if st.button("Evaluate Candidate"):
        if jd and resume:
            score = match_score(jd, resume)

            col1, col2 = st.columns(2)
            col1.metric("Skill Match Score", f"{score}%")

            if score > 75:
                col2.success("High Fit Candidate")
            elif score > 50:
                col2.warning("Moderate Fit Candidate")
            else:
                col2.error("Low Fit Candidate")
        else:
            st.warning("Please enter both Job Description and Resume text.")

# ------------------ MODULE 2 ------------------
elif menu == "Interview Evaluation":
    st.title("Interview Evaluation & Hiring Decision")

    st.caption("Structured interview feedback converted into hiring decisions")

    feedback = st.text_area("Interview Feedback")

    if st.button("Generate Decision"):
        if feedback:
            if "good" in feedback.lower() or "strong" in feedback.lower():
                st.success("Recommended Decision: HIRE")
            else:
                st.error("Recommended Decision: REJECT")
        else:
            st.warning("Please enter interview feedback.")

# ------------------ MODULE 3 ------------------
elif menu == "Engagement & Risk":
    st.title("Candidate Engagement & Drop-Off Risk")

    st.caption("Predicting post-offer engagement risks")

    responses = st.slider(
        "Candidate Interaction Count (emails / calls / replies)",
        0, 5, 1
    )

    if responses < 2:
        st.error("High Drop-Off Risk Detected")
        st.write("Recommended Action: Immediate recruiter follow-up")
    else:
        st.success("Candidate Engagement is Healthy")

# ------------------ CHATBOT ------------------
elif menu == "Hiring Assistant":
    st.title("Hiring Assistant Chatbot")

    st.caption("Natural language interface for recruiters & managers")

    query = st.text_input("Ask a hiring question")

    if query:
        q = query.lower()
        if "top" in q:
            st.info("Top candidates are ranked based on AI skill-match scores.")
        elif "drop" in q:
            st.warning("Candidate shows a high probability of drop-off.")
        elif "status" in q:
            st.success("Candidate is currently in interview evaluation stage.")
        else:
            st.write("Please ask a hiring-related question.")
