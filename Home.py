import streamlit as st
import nltk
nltk.donwload('all')
st.set_page_config(
        page_title="Disaster Tweets",
)

st.image('data/5568.jpeg')

st.header('Analysis and classification of Disaster Tweets')
st.write("Twitter has become an important communication channel in times of emergency.")
st.write("The ubiquitousness of smartphones enables people to announce an emergency they’re observing in real-time. Because of this, more agencies are interested in programatically monitoring Twitter (i.e. disaster relief organizations and news agencies).")
st.write("The app is an attempt at analyzing disaster tweets against non disaster tweets and classifying a given tweet into one of these categories.")
