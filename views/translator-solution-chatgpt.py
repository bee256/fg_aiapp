import streamlit as st
import ollama

# Supported languages
LANGUAGES = {
    "English": "English",
    "Spanish": "Spanish",
    "French": "French",
    "German": "German",
    "Chinese": "Chinese",
    "Japanese": "Japanese",
    "Korean": "Korean",
    "Italian": "Italian",
    "Portuguese": "Portuguese",
}

def create_prompt(text, target_language):
    """
    Creates a prompt for the LLM to perform translation.
    """
    return f"Translate the following text into {target_language}:\n\n{text}"


def response_generator():
    ollama_response = ollama.chat(model=st.session_state.sel_mod['model'], stream=True, messages=st.session_state.messages)
    for partial_resp in ollama_response:
        token = partial_resp["message"]["content"]
        # st.session_state["full_message"] += token
        yield token


# Streamlit app
st.title("AI Translator")

# Input field
input_text = st.text_area("Enter the text to translate:", "")

# Dropdown for target language
target_language = st.selectbox("Select the target language:", list(LANGUAGES.values()))

# Translate button
if st.button("Translate"):
    if input_text.strip():
        # Create a prompt for the LLM
        prompt = create_prompt(input_text, target_language)
        st.session_state.messages = [{"role": "user", "content": prompt}]

        st.success("Translation")
        st.write_stream(response_generator())
    else:
        st.warning("Please enter text to translate.")