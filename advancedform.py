import streamlit as st
from datetime import datetime

min_date=datetime(1990,1,1)
max_date=datetime.now()

st.title("User Information Form")

with st.form(key="User_Info_form",clear_on_submit=True):
  name=st.text_input("Enter your Name")

  birthdate=st.date_input("Enter your birthdate",min_value=min_date,max_value=max_date)

  if birthdate:
    age=max_date.year-birthdate.year
    if birthdate.month>max_date.month or (birthdate.month==max_date.month and birthdate.day>max_date.day):
      age-=1
    st.write(f"Your calculated age is {age} years")

  submit_button=st.form_submit_button()

  if submit_button:
    if not name or not birthdate:
      st.warning("Please fill all fields")
    else:
      st.success(f"Thank you {name}, your age is {age}")
      st.balloons()
      
