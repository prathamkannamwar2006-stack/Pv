
import streamlit as st

st.set_page_config(
    page_title="My Developer Portfolio",
    page_icon="💻",
    layout="wide",
)

# Sidebar
with st.sidebar:
    st.title("👨‍💻 My Portfolio")
    st.write("Python Developer")
    st.markdown("---")
    st.write("📧 your.email@example.com")
    st.write("🔗 [GitHub](https://github.com/YOUR_USERNAME)")
    st.write("💼 [LinkedIn](https://www.linkedin.com/)")

# Home
st.title("Hello, I'm Your Name 👋")
st.subheader("Aspiring Python Developer")

st.write(
    "Welcome to my portfolio! I enjoy building applications, "
    "solving problems, and learning new technologies."
)

st.markdown("---")

# About
st.header("🙋 About Me")
st.write(
    "I am a developer interested in Python, web development, "
    "automation, and building useful software projects."
)

# Skills
st.header("🛠️ Skills")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Programming")
    st.write("- Python")
    st.write("- SQL")
    st.write("- JavaScript")

with col2:
    st.subheader("Tools")
    st.write("- Git")
    st.write("- GitHub")
    st.write("- VS Code")

with col3:
    st.subheader("Frameworks")
    st.write("- Streamlit")
    st.write("- Flask")
    st.write("- FastAPI")

st.markdown("---")

# Projects
st.header("🚀 My Projects")

projects = [
    {
        "name": "Expense Tracker",
        "description": "Track expenses and visualize spending.",
        "github": "https://github.com/YOUR_USERNAME/expense-tracker",
    },
    {
        "name": "Weather App",
        "description": "Display weather information using an API.",
        "github": "https://github.com/YOUR_USERNAME/weather-app",
    },
    {
        "name": "Python Automation",
        "description": "Automate repetitive everyday tasks.",
        "github": "https://github.com/YOUR_USERNAME/python-automation",
    },
]

for project in projects:
    with st.container(border=True):
        st.subheader(project["name"])
        st.write(project["description"])
        st.link_button("View on GitHub", project["github"])

# Contact
st.markdown("---")
st.header("📬 Contact Me")

st.write("Interested in collaborating? Send me a message.")

with st.form("contact_form"):
    name = st.text_input("Your name")
    email = st.text_input("Your email")
    message = st.text_area("Your message")

    submitted = st.form_submit_button("Submit")

    if submitted:
        if name.strip() and email.strip() and message.strip():
            st.success(
                "Thanks for your interest! "
                "This demo does not send messages yet."
            )
        else:
            st.warning("Please complete all fields.")

st.caption("© 2026 Your Name | Built with Python and Streamlit")
