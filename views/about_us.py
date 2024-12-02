import streamlit as st

from forms.contact import contact_form


# @st.experimental_dialog("Contact Me")
# def show_contact_form():
#     contact_form()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/fg_logo.png", width=230)

with col2:
    st.title("FG Software AG", anchor=False)
    st.write(
        "We make software for fun, and to learn how to code. Everything is possible."
    )
    # if st.button("✉️ Contact Me"):
    #     show_contact_form()


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("How to join", anchor=False)
st.write(
    """
    - 7 Years experience extracting actionable insights from data
    - Strong hands-on experience and knowledge in Python and Excel
    - Good understanding of statistical principles and their respective applications
    - Excellent team-player and displaying a strong sense of initiative on tasks
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("What do you need", anchor=False)
st.write(
    """
    - Programming: Python (Scikit-learn, Pandas), SQL, VBA
    - Data Visualization: PowerBi, MS Excel, Plotly
    - Modeling: Logistic regression, linear regression, decision trees
    - Databases: Postgres, MongoDB, MySQL
    """
)
