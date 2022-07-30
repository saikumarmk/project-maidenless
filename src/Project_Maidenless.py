import streamlit as st
import pandas as pd 
import numpy as np 

with open('src/assets/nomaidens.ogg','rb') as file:
    nomaidens_audio = file.read()


def main():

    st.title("Project Maidenless")
    
    st.audio(nomaidens_audio,format='audio/ogg')

if __name__ == "__main__":
    main()