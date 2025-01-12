import ollama
import streamlit as st
import pandas as pd
import humanize

models = ollama.list()['models']
# Create a dict with the name of the mode as key
models_dict = { item['model']: item for item in models }

# sel_mod_name = st.selectbox("Choose LLM:", models_dict.keys(), on_change=clear_messages)
models_list = list(models_dict.keys())
index = 0
if 'sel_mod' in st.session_state:
    index = models_list.index(st.session_state.sel_mod['model'])
sel_mod_name = st.selectbox("Choose LLM:", models_dict.keys(), index=index)
sel_mod = models_dict[sel_mod_name]
st.session_state.sel_mod = sel_mod

# Create a DataFrame
data = [["Size", humanize.naturalsize(sel_mod['size'])], ["Parameters", sel_mod['details']['parameter_size']]]
st.write(sel_mod)

# Display without header
df = pd.DataFrame(data)
st.subheader('LLM details')
st.write(df.to_html(header=False, index=False), unsafe_allow_html=True)



