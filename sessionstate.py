import streamlit as st

# counter=0

# st.write(f"Counter value : {counter}")

# if st.button("increment"):
#   counter+=1
#   st.write(f"counter incremented to: {counter}")
# else:
#   st.write(f"Counter stays  : {counter}")


if "counter" not in st.session_state:
  st.session_state.counter=0

if st.button("Increment"):
  st.session_state.counter+=1
  st.write(f"Counter incremented to {st.session_state.counter}")

if st.button("reset"):
  st.session_state.counter=0


st.write(f"counter value : {st.session_state.counter}")