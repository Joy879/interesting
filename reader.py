import streamlit as st
# import time
# import glob
import os

import pyttsx3
import PyPDF2

pdf_book = open('THE FALLING OF THE LEAVES.pdf','rb')
pdf_reader = PyPDF2.PdfReader(pdf_book)
num_pages_counter = len(pdf_reader.pages)

st.image(image='https://marvistamom.com/wp-content/uploads/books3.jpg')
play = pyttsx3.init()
st.write(' Audio Book from pdf')
if st.button('Read'):
    for num in range(0, num_pages_counter):
        page = pdf_reader.pages[num]
        data = page.extract_text()

        st.audio(data=play.say(data))
        # st.progress(value=num)
        play.runAndWait()

        st.write('Book is Finished, Thank you!')
        st.balloons()

