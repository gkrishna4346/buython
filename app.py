#python
import streamlit as st


# ---------- Page Config ----------
st.set_page_config(
    page_title="Buy-thon",
    page_icon="🥤",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------- Title ----------
st.title("Buy-thon")
st.subheader("Smart Vending Machine powered by Python")


# ---------- Session State ----------
if "shopping_started" not in st.session_state:
    st.session_state["shopping_started"] = False


# ---------- Start Shopping ----------
if st.button("Start Shopping"):
    st.session_state["shopping_started"] = True


# ---------- Product Selection ----------
if st.session_state["shopping_started"]:

    st.write("Select your product")

    product = st.selectbox(
        "Products",
        [
            "Select Product",
            "Coffee ☕",
            "Juice 🧃",
            "Chips 🍟"
        ],
        key="selected_product"
    )

    if product != "Select Product":
        st.write(f"Selected: {product}")

