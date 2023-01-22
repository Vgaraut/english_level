import streamlit as st
import edit_text


st.title('Title')

st.write('Load your subtitles')

sub = st.file_uploader("load subtitles")

