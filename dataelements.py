import streamlit as st
import pandas as pd

st.title("Streamlit Elements ")


st.subheader("Dataframe")

# Data frame section

df=pd.DataFrame(
  {
    'Name':['Sam','Akash','Santhosh','kumar'],
    'Age':[20,19,21,23],
    'Occupation':['Engineer','Doctor','Artist','nurse']
  }
)

st.dataframe(df)


# Data Edictor section

st.subheader("Data Editor")
editable_df=st.data_editor(df)

# Static Table Section

st.subheader("Static Table")
st.table(df)

# Metrics section

st.subheader("Metrics")
st.metric(label="Total rows",value=len(df))
st.metric(label="Average age", value=round(df['Age'].mean(),1))


# Json and DICT

st.subheader("JSON format")
sample_data={
  'Name':'Sam',
  'Age':20,
  'Occupation':'Engineer'
}

st.json(sample_data)


st.subheader("Dictionary")
st.write(sample_data)