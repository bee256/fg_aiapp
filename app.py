import streamlit as st
from settings import Settings

# --- PAGE SETUP ---
about_us_page = st.Page(
    "views/about_us.py",
    title="About us",
    icon=":material/account_circle:",
    default=True,
)
chatbot_page = st.Page(
    "views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)
translator_page = st.Page(
    "views/translator.py",
    title="Translator",
    icon=":material/translate:",
)
settings_page = st.Page(
    "views/settings_view.py",
    title="Choose LLM",
    icon=":material/smart_toy:",
)

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_us_page],
        "Projects": [chatbot_page, translator_page],
        "Settings": [settings_page]
    }
)


# --- SHARED ON ALL PAGES ---
st.logo("assets/fg_logo_string.png", size="large")
st.sidebar.markdown("Made with ❤️ by FG Software AG")

# Setup settings which is a singleton, if not already stored in session state.
if 'settings' not in st.session_state:
    st.session_state.settings = Settings()

if st.session_state.settings.selected_model is None:
    st.warning("No ollama models found. Please setup ollama first.")

# --- RUN NAVIGATION ---
pg.run()
