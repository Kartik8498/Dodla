import streamlit as st

# ──────────────────────────────────────────────
# PAGE CONFIG
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="Dodla Dairy",
    page_icon="🥛",
    layout="wide"
)

# ──────────────────────────────────────────────
# SESSION STATE
# ──────────────────────────────────────────────
if "city" not in st.session_state:
    st.session_state.city = None
if "cart" not in st.session_state:
    st.session_state.cart = {}

# ──────────────────────────────────────────────
# DATA
# ──────────────────────────────────────────────
CITIES = ["Hyderabad", "Bangalore", "Chennai", "Vijayawada", "Tirupati"]

PRODUCTS = [
    {"name": "Full Cream Milk", "price": 68},
    {"name": "Toned Milk", "price": 44},
    {"name": "Curd", "price": 55},
    {"name": "Paneer", "price": 90},
]

# ──────────────────────────────────────────────
# HELPERS
# ──────────────────────────────────────────────
def add_to_cart(name, price):
    if name in st.session_state.cart:
        st.session_state.cart[name]["qty"] += 1
    else:
        st.session_state.cart[name] = {"qty": 1, "price": price}

def total():
    return sum(v["qty"] * v["price"] for v in st.session_state.cart.values())

# ──────────────────────────────────────────────
# CITY SELECT
# ──────────────────────────────────────────────
if st.session_state.city is None:
    st.title("🥛 Welcome to Dodla Dairy")
    st.write("Select your city")

    cols = st.columns(len(CITIES))
    for i, c in enumerate(CITIES):
        if cols[i].button(c):
            st.session_state.city = c
            st.rerun()

    st.stop()

# ──────────────────────────────────────────────
# HEADER
# ──────────────────────────────────────────────
st.markdown(f"""
### 🚚 Free Delivery | Delivering in **{st.session_state.city}**
""")

# ──────────────────────────────────────────────
# HERO SECTION (FIXED)
# ──────────────────────────────────────────────
st.markdown(f"""
<div style="
    background: linear-gradient(135deg, #003087, #0055C8);
    padding:40px;
    border-radius:20px;
    color:white;
    text-align:center;
">
    <h1>Fresh Milk Delivered Daily 🥛</h1>
    <p>Pure dairy products delivered in {st.session_state.city}</p>
</div>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────
# PRODUCTS
# ──────────────────────────────────────────────
st.subheader("🛍️ Products")

cols = st.columns(4)

for i, p in enumerate(PRODUCTS):
    with cols[i % 4]:
        st.markdown(f"**{p['name']}**")
        st.write(f"₹{p['price']}")

        if st.button("Add", key=p["name"]):
            add_to_cart(p["name"], p["price"])

# ──────────────────────────────────────────────
# CART
# ──────────────────────────────────────────────
st.subheader("🛒 Cart")

if not st.session_state.cart:
    st.info("Cart is empty")
else:
    for name, d in st.session_state.cart.items():
        st.write(f"{name} x {d['qty']} = ₹{d['qty'] * d['price']}")

    st.markdown(f"### Total: ₹{total()}")

    if st.button("Checkout"):
        st.success("Order placed!")
        st.session_state.cart = {}
