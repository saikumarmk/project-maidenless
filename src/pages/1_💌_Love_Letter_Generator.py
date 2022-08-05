import streamlit as st
from aitextgen import aitextgen
import tokenizers

@st.cache(hash_funcs={tokenizers.Tokenizer: lambda _: None, tokenizers.AddedToken: lambda _: None})
def load_models():

    return aitextgen(model_folder='uom_mll_model')


ai_all = load_models()

st.title("GPT-2 - Love Letter Generator")

st.markdown("This model has been trained on over 17,000 letters from UoM Love Letters, and Monash University Love Letters. Avoid modifying the last two arguments if you don't know what they do.")

prompt = st.text_input(label="Enter a prompt to create a letter...")


with st.form("Parameters"):

    #n = st.number_input("Number of letters", min_value=1,
    #                     max_value=30, value=1)
    
    min_length = st.number_input(
        "Minimum length of letter", min_value=20, max_value=100, value=20)
    max_length = st.number_input(
        "Maximum length of letter", min_value=40, max_value=250, value=50)
    temperature = st.number_input(
        "Craziness", min_value=0.0, max_value=1.0, value=0.7)
    top_k = st.number_input("Top k", min_value=0, max_value=30, value=0)
    top_p = st.number_input("Top p", min_value=0.0, max_value=1.0, value=0.9)
    #source = st.selectbox("Page", ("All",'TBA'))

    submit = st.form_submit_button("Run!")

if submit:

    with st.spinner("Spinning up a letter..."):
        source = "All"
        # TODO: add different letters
        match source:
            case _:
                generated_messages = ai_all.generate_one(
                    prompt=prompt, temperature=temperature, top_k=top_k, top_p=top_p,min_length=min_length,max_length=max_length)

                st.balloons()

    st.markdown(generated_messages)
