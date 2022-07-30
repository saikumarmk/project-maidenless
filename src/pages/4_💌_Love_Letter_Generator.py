import streamlit as st
from aitextgen import aitextgen


ai = aitextgen()

st.title("GPT-2 - Love Letter Generator")

with st.sidebar:
    n = st.number_input("Number of letters", min_value=1, max_value=30,value=1)
    max_length = st.number_input(
        "Maximum length of letter", min_value=20, max_value=250,value=30)
    temperature = st.number_input("Craziness", min_value=0.0, max_value=1.0,value=0.7)
    top_k = st.number_input("Top k", min_value=0, max_value=30)
    top_p = st.number_input("Top p", min_value=0.0, max_value=1.0)
    source = st.selectbox("Page",("Monash","Melbourne","All"))

prompt = st.text_input(label="Enter a prompt to create a letter...")

if st.button("Run!"):
    with st.spinner("Spinning up a letter..."):
        generated_messages = ai.generate_one(
            prompt=prompt, temperature=temperature)


    st.balloons()

    st.text(generated_messages)
