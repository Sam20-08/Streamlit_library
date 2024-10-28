import streamlit as st
import os

st.title("This is Title")
st.header("This is header")
st.subheader("Sub header")
st.markdown("This is _Markdown_")
st.caption("small text")


# Code rendering

code_example="""
def greet():
  print("hello",name)
"""

st.code(code_example,language="python")

st.divider()

st.image(os.path.join(os.getcwd(),"static","sample.jpg"))