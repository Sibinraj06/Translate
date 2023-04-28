import streamlit as st
from googletrans import  Translator 
st.header("Machine translation demo")
input = st.text_area("Please type the text here", value='')
option = st.selectbox('To which language you wisj to translate this text too',('Malayalam','Tamil','Hindi'))
if st.button("Translate"):
    translator = Translator()
    translation= translator.translate(input, dest=option)
    st.write(translation.text)


