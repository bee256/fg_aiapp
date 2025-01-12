import streamlit as st

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/fg_logo.png", width=230)

with col2:
    st.title("FG Software AG", anchor=False)
    st.write(
        "Wir machen Software »just for fun«. Wir probieren aus, lernen zu programmieren und grundsätzlich gilt: alles ist möglich."
    )

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Wie kann ich mitmachen?", anchor=False)
st.write(
    """
    - Komm einfach Montags in den FG Rechnerraum zwischen 17:00 und 19:00 Uhr 
    - Wenn du schon etwas programmieren kannst, ist es von Vorteil. Falls nicht, dann zeigen wir dir, wie du einsteigen kannst.
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Was muss ich mitbringen", anchor=False)
st.write(
    """
    - Spass am selber programmieren
    - Etwas Durchhaltevermögen (es klappt nicht immer gleich) 😬
    """
)
