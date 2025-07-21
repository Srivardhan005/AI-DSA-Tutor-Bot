with open("app.py", "w") as f:
    f.write('''
import streamlit as st
from gemini_chat import GeminiChat

st.set_page_config(page_title="DSA Tutor", layout="centered")

# ------------------ UI Header ------------------
st.title("📘 AI DSA Tutor")
st.markdown("Get DSA questions and solutions powered by Gemini!")

# ------------------ API Key Input ------------------
api_key = st.text_input("🔑 Enter your Gemini API Key", type="password")

if api_key:
    gemini = GeminiChat(api_key=api_key)

    # ------------------ Topic Dropdown ------------------
    topic = st.selectbox("📂 Select DSA Topic", [
        "Arrays", "Linked List", "Stacks", "Queues",
        "Trees", "Graphs", "Searching", "Sorting",
        "Dynamic Programming", "Greedy Algorithms"
    ])

    # ------------------ Level Selector ------------------
    level = st.radio("📊 Choose Difficulty", ["Easy", "Medium"])

    # ------------------ Question Prompt + Button ------------------
    if st.button("🎯 Generate Sample Question"):
        prompt = f"Give me a {level} level coding problem on {topic}. Return only the problem statement."
        question = gemini.send_message(prompt)
        st.subheader("🧩 Question")
        st.markdown(question)

    # ------------------ User Custom Prompt ------------------
    user_prompt = st.text_area("✍️ Ask anything else:")
    if st.button("💬 Ask Gemini"):
        if user_prompt.strip():
            response = gemini.send_message(user_prompt)
            st.subheader("📜 Answer")
            st.markdown(response)
        else:
            st.warning("Please enter a question.")
else:
    st.warning("Please enter your API key to start.")
''')
