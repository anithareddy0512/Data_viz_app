import streamlit as st

st.title("Welcome to my First Data App")
st.snow()

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :cry:")
    st.balloons()