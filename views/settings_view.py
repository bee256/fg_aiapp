import streamlit as st
import pandas as pd
import humanize

from settings import Settings


settings = Settings()
index = 0
if settings.selected_model:
    index = settings.models_list.index(settings.selected_model['model'])

sel_mod_name = st.selectbox("Choose LLM:", settings.models_list, index=index)

if sel_mod_name:
    settings.set_model(sel_mod_name)

    # Create a DataFrame
    data = [["Size", humanize.naturalsize(settings.selected_model['size'])], ["Parameters", settings.selected_model['details']['parameter_size']]]
    st.write(settings.selected_model)

    # Display without header
    df = pd.DataFrame(data)
    st.subheader('LLM details')
    st.write(df.to_html(header=False, index=False), unsafe_allow_html=True)
