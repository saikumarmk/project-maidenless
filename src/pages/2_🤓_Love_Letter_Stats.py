import pandas as pd 
import streamlit as st
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt 

st.set_page_config("Love Letter Stats", "nerd_face")

st.title("Love Letter infographics")

with st.sidebar:
    st.selectbox("University",("Monash","Melbourne"))


st.markdown("Coming soon.")