import streamlit as st
st.set_page_config(
    page_title = "Buy-thon",
    page_icon = "🥤",
    layout = "wide",
    initial_sidebar_state = "expanded"
)

st.title ("Buy-thon")
st.subheader("Smart Vending Machine powered by Python")

if st.button("Start Shopping"):
    st.write("Welcome to Buy-thon 🥤")