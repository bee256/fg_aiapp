import streamlit as st
import ollama


def create_prompt(text):
    """
    Creates a prompt for the LLM to perform translation.
    """
    prompt = """
Refine the writing of the given text style to convey ideas with precision and impact. Pay attention to the
appropriate tone for the intended audience, whether it be formal, informal, persuasive, or informative.
Focus on clarity by organizing thoughts logically, avoiding ambiguity, and providing clear transitions between ideas.
Strive for conciseness by eliminating unnecessary wordiness and refining sentences for brevity without sacrificing clarity.
If the input text has another language than english, identify the language and output the new text in the language of the input text
"""
    prompt = prompt.strip()

    return f"{prompt}:\n\n{text}"


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
st.title("AI Text optimizer")

if not 'input_history' in st.session_state:
    # initialise an empty array
    st.session_state.input_history = []

# Create two columns
col1, col2 = st.columns([2, 1])
# Input field
with col2:
    selected_option = st.selectbox("History:", st.session_state.input_history)
with col1:
    input_text = st.text_area("Enter the text to optimize:", selected_option)

# Dropdown for target language
# target_language = st.selectbox("Select the target language:", list(LANGUAGES.values()))

# Translate button
if st.button("Optimize", on_click=update_history(input_text)):
    if input_text and not input_text.isspace():
        input_text = input_text.strip()
        # Create a prompt for the LLM
        prompt = create_prompt(input_text)

        st.success("Optimized text")
        st.write_stream(response_generator(prompt))
    else:
        st.warning("Please enter a text to translate.")
