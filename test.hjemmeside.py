import streamlit as st
from ai_logic import Modelgenerator # Importerer din klasse

st.set_page_config(page_title="AI 3D Test", page_icon="🤖")

st.title("Test av AI-Generator")
st.write("Dette er en midlertidig side for å sjekke at f.ai_logic.py fungerer.")

# Bruker @st.cache_resource så modellen ikke lastes på nytt hver gang du trykker
@st.cache_resource
def get_ai_engine():
    return Modelgenerator()

with st.spinner("Laster inn AI-modellen (dette tar litt tid første gang)..."):
    engine = get_ai_engine()

# Brukergrensesnitt
user_prompt = st.text_input("Hva vil du generere?", "a simple boat")

if st.button("Generer 3D-fil"):
    with st.spinner(f"Genererer '{user_prompt}'..."):
        # Her kaller vi på din metode!
        output_file = engine.generate(user_prompt)
        
        st.success(f"Suksess! Filen er lagret som: {output_file}")
        st.info("Du finner filen i prosjektmappen din nå.")