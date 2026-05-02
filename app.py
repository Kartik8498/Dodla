import streamlit as st
from PIL import Image

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Dodla Dairy",
    page_icon="🥛",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --------------------------------------------------
# LOAD LOGO
# --------------------------------------------------
logo = Image.open("assets/logo.png")

# --------------------------------------------------
# PREMIUM STYLES
# --------------------------------------------------
st.markdown("""
<style>
html, body, [class*="css"] {
    background:#ffffff !important;
    font-family:'Poppins', sans-serif;
}

.topbar {
    background:#fff5f5;
    color:#e53e4d;
    text-align:center;
    padding:10px;
    border-radius:0 0 18px 18px;
    font-weight:600;
}

.navbar {
    background:white;
    padding:12px;
    border-radius:20px;
    box-shadow:0 8px 25px rgba(0,0,0,0.05);
    margin-bottom:20px;
}

.hero {
    background:#fff1f1;
    padding:40px;
    border-radius:25px;
    margin-top:10px;
    box-shadow:0 15px 40px rgba(0,0,0,0.05);
}

.card {
    background:white;
    padding:16px;
    border-radius:20px;
    box-shadow:0 10px 30px rgba(0,0,0,0.08);
}

.price {
    color:#e53e4d;
    font-weight:bold;
    font-size:18px;
}

.stButton button {
    background:#e53e4d;
    color:white;
    border-radius:25px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SESSION
# --------------------------------------------------
if "cart" not in st.session_state:
    st.session_state.cart = {}

def add_to_cart(name, price):
    if name in st.session_state.cart:
        st.session_state.cart[name]["qty"] += 1
    else:
        st.session_state.cart[name] = {"qty": 1, "price": price}

def cart_total():
    return sum(v["qty"] * v["price"] for v in st.session_state.cart.values())

def cart_count():
    return sum(v["qty"] for v in st.session_state.cart.values())

# --------------------------------------------------
# TOP BAR
# --------------------------------------------------
st.markdown(
    '<div class="topbar">🚚 Free delivery above ₹299 | Fresh dairy since 1995</div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# NAVBAR WITH LOGO
# --------------------------------------------------
nav1, nav2, nav3 = st.columns([1,3,1])

with nav1:
    st.image(logo, width=110)

with nav2:
    st.text_input("", placeholder="Search products...")

with nav3:
    st.markdown(f"### 🛒 {cart_count()}")

# --------------------------------------------------
# HERO
# --------------------------------------------------
st.markdown("""
<div class="hero">
<h1 style="color:#e53e4d;">Fresh dairy delivered beautifully</h1>
<p>Premium Dodla products delivered to your doorstep</p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# PRODUCTS
# --------------------------------------------------
products = [
    {"name": "Toned Milk", "price": 44},
    {"name": "Curd", "price": 55},
    {"name": "Paneer", "price": 90},
    {"name": "Cow Ghee", "price": 584},
]

st.markdown("## 🛍️ Products")

cols = st.columns(4)

for i, p in enumerate(products):
    with cols[i]:
        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.markdown(f"**{p['name']}**")
        st.markdown(f"<div class='price'>₹{p['price']}</div>", unsafe_allow_html=True)

        if st.button("Add to Cart", key=p["name"]):
            add_to_cart(p["name"], p["price"])
            st.success("Added!")

        st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------------------------
# CART
# --------------------------------------------------
st.markdown("## 🛒 Cart")

if not st.session_state.cart:
    st.info("Cart is empty")
else:
    for name, details in st.session_state.cart.items():
        st.write(f"{name} x {details['qty']} = ₹{details['qty'] * details['price']}")

    st.markdown(f"### Total: ₹{cart_total()}")

    if st.button("Checkout"):
        st.success("Order placed!")
        st.session_state.cart = {}

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("""
<hr>
<center style="color:#999;">Dodla Dairy © 2026</center>
""", unsafe_allow_html=True)
