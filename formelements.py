import streamlit as st
import pandas as pd

st.title("Form Elements")

# Form to hold the interactive elements

with st.form(key="sample_form"):
  st.subheader("Text Input")
  name=st.text_input("Enter your name")

  st.text_area("Enter your Feedback")

  # Date and Time
  st.subheader("Date and Time Inputs")
  dob=st.date_input("Select your date of birth")
  time=st.time_input("Choose a preferred time")

  # Selectors

  st.subheader("selectors")
  choice=st.radio("choose an option",["Option 1","Option 2","Option 3"])
  gender=st.selectbox("Select your gender",["Male","Female"])
  slider_value=st.select_slider("selecct a range",options=[1,2,3,4,5,6]) 

  # TOggles and checkboxes
  st.subheader("Toogles and checkboxes")
  notification=st.checkbox("Receive notification")
  toggle_value=st.checkbox("Enable dark mode? ",value=False)

  # Submit button for the form
  submit_button=st.form_submit_button(label="submit")