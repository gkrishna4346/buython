import streamlit as st


# ---------- PAGE ----------
st.set_page_config(
    page_title="Buy-thon",
    page_icon="🥤",
    layout="wide"
)


# ---------- SESSION ----------
if "shopping_started" not in st.session_state:
    st.session_state["shopping_started"] = False

if "cart" not in st.session_state:
    st.session_state["cart"] = {}


# ---------- HEADER ----------
left_header, right_header = st.columns(
    [2, 1]
)


# ---------- LEFT ----------
with left_header:

    st.image(
        "images/logo.jpg",
        width=300
    )

    if st.button(
        "Start Shopping"
    ):
        st.session_state[
            "shopping_started"
        ] = True


# ---------- RIGHT ----------
with right_header:

    st.subheader(
        "Cart Summary"
    )

    grand_total = 0

    if st.session_state["cart"]:

        for item, details in (
            st.session_state["cart"]
            .items()
        ):

            total = (
                details["qty"]
                *
                details["price"]
            )

            grand_total += total

            st.write(
                f"{item} × {details['qty']} = ₹{total}"
            )

        st.success(
            f"Current Total: ₹{grand_total}"
        )

        if st.button(
            "Place Order"
        ):

            st.balloons()

            st.success(
                f"Order placed • ₹{grand_total}"
            )

    else:

        st.info(
            "No products added"
        )


st.divider()


# ---------- PRODUCTS ----------
product_sections = {

    "☕ Beverages": {

        "☕ Cold Coffee": 50,
        "🥤 Coke": 50,
        "🥤 Pepsi": 50,
        "🥤 Campa": 40,
        "🥤 Redbull": 100
    },

    "🍟 Snacks": {

        "🍿 Popcorn": 40,
        "🍟 Lays": 40,
        "🍟 Kurkure": 30,
        "🍟 Cheetos": 30,
        "🍜 Cup Noodles": 40
    },

    "🍫 Chocolate": {

        "🍫 Dairy Milk": 50,
        "🍫 5 Star": 40,
        "🍫 Snicker": 50,
        "🍫 Bourneville": 90,
        "🍫 Kitkat": 40
    }
}


# ---------- SHOP ----------
if st.session_state["shopping_started"]:

    col1, col2, col3 = st.columns(
        3
    )

    section_columns = [
        col1,
        col2,
        col3
    ]


    for index, (
        section,
        products
    ) in enumerate(
        product_sections.items()
    ):

        with section_columns[index]:

            with st.container(
                border=True
            ):

                st.subheader(
                    section
                )

                h1, h2, h3 = st.columns(
                    [1.8, 0.6, 0.5]
                )

                with h1:
                    st.caption(
                        "Product"
                    )

                with h2:
                    st.caption(
                        "Qty"
                    )

                with h3:
                    st.caption(
                        "Add"
                    )


                for item, price in (
                    products.items()
                ):

                    c1, c2, c3 = st.columns(
                        [1.8, 0.6, 0.5]
                    )


                    with c1:

                        selected = (
                            st.checkbox(
                                f"{item} • ₹{price}",
                                key=f"check_{item}"
                            )
                        )


                    with c2:

                        quantity = (
                            st.number_input(
                                "",
                                min_value=1,
                                max_value=20,
                                value=1,
                                disabled=(
                                    not selected
                                ),
                                label_visibility="collapsed",
                                key=f"qty_{item}"
                            )
                        )


                    with c3:

                        add = (
                            st.button(
                                "Add",
                                key=f"add_{item}"
                            )
                        )


                    if add:

                        if selected:

                            st.session_state[
                                "cart"
                            ][item] = {

                                "qty": quantity,

                                "price": price
                            }

                        else:

                            st.warning(
                                "Select item"
                            )


                    if not selected:

                        st.session_state[
                            "cart"
                        ].pop(
                            item,
                            None
                        )

st.divider()

st.markdown(
    """
    <div style='
    text-align:center;
    color:gray;
    font-size:14px;
    padding-top:10px;
    '>
    App built by Gopikrishna
    </div>
    """,
    unsafe_allow_html=True
)