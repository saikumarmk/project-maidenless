import streamlit as st
from aitextgen import aitextgen

 
ai =aitextgen(model_folder="savedmodel")

st.title("GPT-2 - Love Letter Generator")



prompt = st.text_input(label="Enter a prompt to create a letter...")


with st.form("Parameters"):
    n = st.number_input("Number of letters", min_value=1, max_value=30,value=1)
    max_length = st.number_input(
        "Maximum length of letter", min_value=20, max_value=250,value=30)
    temperature = st.number_input("Craziness", min_value=0.0, max_value=1.0,value=0.7)
    top_k = st.number_input("Top k", min_value=0, max_value=30,value=0)
    top_p = st.number_input("Top p", min_value=0.0, max_value=1.0,value=0.9)
    source = st.selectbox("Page",("Monash","Melbourne","All"))


    submit = st.form_submit_button("Run!")

if submit:
    
    with st.spinner("Spinning up a letter..."):
        # Match case 
        match source:
            case _:
                generated_messages = ai.generate_one(
                    prompt=prompt, temperature=temperature,top_k=top_k,top_p=top_p)


        st.balloons()

    st.markdown(generated_messages)
