with open("app.py", "w") as f:
    f.write('''
import streamlit as st
from gemini_chat import GeminiChat

# ------------------------- UI Config -------------------------
st.set_page_config(page_title="AI DSA Tutor Bot", layout="centered")
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🤖 AI DSA Tutor Bot</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# ------------------------- Sidebar -------------------------
st.sidebar.header("🔐 Gemini API Key")
api_key = st.sidebar.text_input("Enter your Gemini API Key", type="password")

st.sidebar.markdown("### ℹ️ About")
st.sidebar.info(\"\"\"
AI DSA Tutor Bot helps you learn Data Structures & Algorithms through topic-specific questions.

Built using **Google Gemini API**, **Streamlit**, and **Python**.

Crafted with ❤️ by Srivardhan.
\"\"\")

st.sidebar.markdown("### 💡 Prompt Tips")
st.sidebar.success(
    "- Select a topic & difficulty\\n"
    "- Click 'Get Question'\\n"
    "- Ask for explanations too!"
)

# ------------------------- Main Section -------------------------
if api_key:
    gemini = GeminiChat(api_key=api_key)

    topic = st.selectbox("📘 Select a Topic", ["Array", "Linked List", "Stack", "Queue", "Tree", "Graph", "Sorting", "Searching", "DP", "Recursion"])
    difficulty = st.radio("🧠 Choose Difficulty", ["Easy", "Medium", "Hard"], horizontal=True)

    if st.button("🚀 Get Question"):
        with st.spinner("Thinking..."):
            prompt = f"Generate a {difficulty} level DSA coding question on the topic {topic}. Only give the question."
            response = gemini.send_message(prompt)
            st.markdown("### 📜 Question")
            st.code(response.strip(), language="markdown")
else:
    st.warning("Please enter your API key in the sidebar to continue.")
''')
