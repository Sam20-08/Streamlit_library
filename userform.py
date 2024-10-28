import streamlit as st
from datetime import datetime

st.title("User Information Form")

min_date=datetime(1990,1,1)
max_date=datetime.now()

form_values={
  "name":None,
  "height":None,
  "dob":None,
  "Gender":None,
}

with st.form(key="User_info_details"):
  form_values["name"]=st.text_input("Enter you name")
  form_values["height"]=st.number_input("Enter your height(cm)")
  form_values["dob"]=st.date_input("Enter your Date of birth",min_value=min_date,max_value=max_date)
  form_values["Gender"]=st.selectbox("Gender",["Male","Female"])

  
  submit_button=st.form_submit_button()

  if submit_button:
    if not all(form_values.values()):
      st.warning("please fill all fields")
    else:
      st.balloons()
      st.write("### Info")
      for(key,value) in form_values.items():
        st.write(f"{key} : {value}")