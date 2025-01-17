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


def response_generator(prompt: str):
    ollama_response = ollama.generate(model=st.session_state.settings.get_model_name(), stream=True, prompt=prompt)
    for partial_resp in ollama_response:
        token = partial_resp["response"]
        yield token


def update_history(item: str):
    if not item or item.isspace():
        return
    item = item.strip()
    if item not in st.session_state.input_history:
        st.session_state.input_history.insert(0, item)


# Streamlit app
st.title("AI Translator")

if not 'input_history' in st.session_state:
    # initialise an empty array
    st.session_state.input_history = []

# Create two columns
col1, col2 = st.columns([2, 1])
# Input field
with col2:
    selected_option = st.selectbox("History:", st.session_state.input_history)
with col1:
    input_text = st.text_area("Enter the text to translate:", selected_option)

# Dropdown for target language
target_language = st.selectbox("Select the target language:", list(LANGUAGES.values()))

# Translate button
if st.button("Translate", on_click=update_history(input_text)):
    if input_text and not input_text.isspace():
        input_text = input_text.strip()
        # Create a prompt for the LLM
        prompt = create_prompt(input_text, target_language)

        st.success("Translation")
        st.write_stream(response_generator(prompt))
    else:
        st.warning("Please enter a text to translate.")
