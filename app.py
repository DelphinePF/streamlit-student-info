import streamlit as st
 # Title of the app
st.title("Student Information")
Name = st.text_input("Enter the student name :")
Age = st.slider("Select the student's age:",1)
if st.button("Display information"):
    st.write("Student's Name :",Name)
    st.write("Student's age :", Age)
    