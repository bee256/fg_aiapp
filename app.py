import streamlit as st
from settings import Settings

# --- PAGE SETUP ---
about_page = st.Page(
    "views/about_us.py",
    title="About us",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    "views/sales_dashboard.py",
    title="Demo Dashboard",
    icon=":material/bar_chart:",
)
chatbot_page = st.Page(
    "views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)
translator_page = st.Page(
    "views/translator.py",
    title="Übersetzer",
    icon=":material/translate:",
)
settings_page = st.Page(
    "views/settings_view.py",
    title="Choose LLM",
    icon=":material/smart_toy:",
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, chatbot_page, translator_page],
        "Settings": [settings_page]
    }
)


# --- SHARED ON ALL PAGES ---
st.logo("assets/fg_logo_string.png", size="large")
st.sidebar.markdown("Made with ❤️ by FG Software AG")

# Setup settings which is a singleton, if not already stored in session state.
if 'settings' in st.session_state:
    settings = st.session_state['settings']
else:
    settings = Settings()

if settings.selected_model is None:
    st.warning("No ollama models found. Please setup ollama first.")

# --- RUN NAVIGATION ---
pg.run()
