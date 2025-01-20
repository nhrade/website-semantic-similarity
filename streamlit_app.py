import streamlit as st
from bs4 import BeautifulSoup
import requests
import spacy

nlp = spacy.load("en_core_web_md")


def check_similarity(url1, url2):
    website1_data = requests.get(url1).text
    website2_data = requests.get(url2).text
    text1 = BeautifulSoup(website1_data, "html.parser").get_text()
    text2 = BeautifulSoup(website2_data, "html.parser").get_text()
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    sim = doc1.similarity(doc2)
    return sim


st.write(
    """
# Website Similarity Tool

This tool lets you determine the semantic similarity of two webpages.
Enter the URLs below and then click "Check Similarity" to determine by how much each
website is similar.
         """
)

col1, col2 = st.columns(2)

with col1:
    left_url = st.text_input(label="First URL", placeholder="https://en.wikipedia.org/wiki/Shiva")

with col2:
    right_url = st.text_input(label="Second URL", placeholder="https://en.wikipedia.org/wiki/Yoga")

similarity = 0

if st.button("Check Similarity", type="primary"):
    with st.spinner("Please wait..."):
        similarity = round(check_similarity(left_url, right_url), 4)

st.metric("Similarity", f"{similarity*100}%")
