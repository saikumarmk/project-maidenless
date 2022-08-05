import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config("Project Maidenless", "fire")

with open('src/assets/nomaidens.ogg', 'rb') as file:
    nomaidens_audio = file.read()


def main():

    st.title("Project Maidenless")

    st.markdown("## What is this?\n For now, this app is just a love letter generator for Monash and UoM, trained on 17,000 letters on both page.")

    st.markdown("## Future goals\n Since the data I've scraped is primarily text-based, a goal I have is to index and archive letters from the page, as Facebook often makes it hard to search for past letters, or the page may be deleted.")

    

    st.audio(nomaidens_audio, format='audio/ogg')


if __name__ == "__main__":
    main()
