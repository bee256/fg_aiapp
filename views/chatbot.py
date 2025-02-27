import ollama
import streamlit as st


def clear_messages():
    st.session_state.messages = []


def response_generator():
    ollama_response = ollama.chat(model=st.session_state.settings.get_model_name(), stream=True,
                                  messages=st.session_state.messages)
    for partial_resp in ollama_response:
        token = partial_resp["message"]["content"]
        st.session_state["full_message"] += token
        yield token


# Custom CSS for a fixed "New Chat" button
st.markdown(
    """
    <style>
    .new-chat-button {
        position: fixed;
        top: 10px;
        right: 10px;
        z-index: 9999;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# "New Chat" button functionality
if st.button("New Chat", key="new_chat", args=None, kwargs=None, help=None, on_click=None, type="primary", disabled=False, use_container_width=False):
    # Initialize chat history
    clear_messages()
    st.success("Chat history has been reset!")


st.title("💬 FG Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    clear_messages()    # to create the empty array

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    if prompt.strip():
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.session_state["full_message"] = ""
            response = st.write_stream(response_generator())
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": st.session_state["full_message"]})
