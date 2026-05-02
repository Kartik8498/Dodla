import streamlit as st
from PIL import Image

# ──────────────────────────────────────────────
# CONFIG
# ──────────────────────────────────────────────
st.set_page_config(page_title="Dodla Dairy", page_icon="🥛", layout="wide")

# ──────────────────────────────────────────────
# LOAD IMAGES
# ──────────────────────────────────────────────
logo = Image.open("assets/logo.png")
milk = Image.open("assets/milk.png")
curd = Image.open("assets/curd.png")
paneer = Image.open("assets/paneer.png")
ghee = Image.open("assets/ghee.png")

# ──────────────────────────────────────────────
# SESSION STATE
# ──────────────────────────────────────────────
if "cart" not in st.session_state:
    st.session_state.cart = {}

def add_to_cart(name, price):
    if name in st.session_state.cart:
        st.session_state.cart[name]["qty"] += 1
    else:
        st.session_state.cart[name] = {"qty": 1, "price": price}

def total():
    return sum(v["qty"] * v["price"] for v in st.session_state.cart.values())

def total_items():
    return sum(v["qty"] for v in st.session_state.cart.values())

# ──────────────────────────────────────────────
# PREMIUM CSS
# ──────────────────────────────────────────────
st.markdown("""
<style>
html, body, [class*="css"] {
    background-color: #FFFFFF;
    font-family: 'Poppins', sans-serif;
}

/* HEADER */
.header {
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:10px 0;
}

/* HERO */
.hero {
    background:#FFF1F1;
    padding:50px;
    border-radius:25px;
    margin-top:20px;
    box-shadow:0 10px 40px rgba(0,0,0,0.05);
}

/* PRODUCT CARD */
.card {
    background:white;
    padding:15px;
    border-radius:20px;
    text-align:center;
    box-shadow:0 10px 30px rgba(0,0,0,0.08);
    transition:0.2s;
}
.card:hover {
    transform:translateY(-6px);
}

/* BUTTON */
.stButton button {
    background:#E5484D;
    color:white;
    border-radius:25px;
    border:none;
    padding:8px 12px;
}

/* PRICE */
.price {
    color:#E5484D;
    font-weight:bold;
    font-size:18px;
}

/* CART BOX */
.cart-box {
    background:#FFF5F5;
    padding:20px;
    border-radius:20px;
    margin-top:20px;
}
</style>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────
# HEADER
# ──────────────────────────────────────────────
col1, col2, col3 = st.columns([1,4,1])

with col1:
    st.image(logo, width=120)

with col2:
    st.markdown("### Fresh Dairy Delivered Daily")

with col3:
    st.markdown(f"### 🛒 {total_items()}")

# ──────────────────────────────────────────────
# HERO
# ──────────────────────────────────────────────
st.markdown("""
<div class="hero">
<h1 style="color:#E5484D;">Fresh dairy delivered beautifully</h1>
<p style="color:#555;">Premium Dodla products delivered to your doorstep</p>
</div>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────
# PRODUCTS
# ──────────────────────────────────────────────
products = [
    {"name": "Toned Milk", "price": 44, "img": milk},
    {"name": "Curd", "price": 55, "img": curd},
    {"name": "Paneer", "price": 90, "img": paneer},
    {"name": "Cow Ghee", "price": 584, "img": ghee},
]

st.markdown("## 🛍️ Our Products")

cols = st.columns(4)

for i, p in enumerate(products):
    with cols[i]:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.image(p["img"], use_column_width=True)
        st.markdown(f"**{p['name']}**")
        st.markdown(f"<div class='price'>₹{p['price']}</div>", unsafe_allow_html=True)

        if st.button("Add to Cart", key=p["name"]):
            add_to_cart(p["name"], p["price"])
            st.success(f"{p['name']} added!")

        st.markdown('</div>', unsafe_allow_html=True)

# ──────────────────────────────────────────────
# CART
# ──────────────────────────────────────────────
st.markdown("## 🛒 Your Cart")

if not st.session_state.cart:
    st.info("Cart is empty")
else:
    st.markdown('<div class="cart-box">', unsafe_allow_html=True)

    for name, details in st.session_state.cart.items():
        st.write(f"{name} x {details['qty']} = ₹{details['qty'] * details['price']}")

    st.markdown(f"### Total: ₹{total()}")

    if st.button("Checkout"):
        st.success("🎉 Order placed successfully!")
        st.session_state.cart = {}

    st.markdown('</div>', unsafe_allow_html=True)

# ──────────────────────────────────────────────
# FOOTER
# ──────────────────────────────────────────────
st.markdown("""
<hr>
<center style="color:#888;">
Dodla Dairy © 2026 • Premium Dairy Experience
</center>
""", unsafe_allow_html=True)
