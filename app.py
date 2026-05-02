import streamlit as st

# ──────────────────────────────────────────────
# PAGE CONFIG
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="Dodla Dairy",
    page_icon="🥛",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ──────────────────────────────────────────────
# GLOBAL STYLES
# ──────────────────────────────────────────────
st.markdown("""
<style>
  /* ---- Google Font ---- */
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

  html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }

  /* ---- Brand palette ---- */
  :root {
    --dodla-blue:   #003087;
    --dodla-gold:   #F5A623;
    --dodla-light:  #EAF3FF;
    --dodla-white:  #FFFFFF;
    --dodla-gray:   #F7F8FA;
    --dodla-text:   #1A1A2E;
  }

  /* ---- Remove default Streamlit padding ---- */
  .block-container { padding-top: 0 !important; }
  #MainMenu, footer, header { visibility: hidden; }

  /* ---- TOP NAV BAR ---- */
  .topbar {
    background: var(--dodla-blue);
    color: white;
    text-align: center;
    padding: 8px;
    font-size: 13px;
    letter-spacing: 0.5px;
  }
  .navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 14px 40px;
    background: white;
    box-shadow: 0 2px 12px rgba(0,0,0,0.08);
    position: sticky; top: 0; z-index: 999;
  }
  .navbar-logo { font-size: 26px; font-weight: 700; color: var(--dodla-blue); }
  .navbar-logo span { color: var(--dodla-gold); }
  .navbar-right { display: flex; gap: 20px; align-items: center; }
  .nav-link {
    text-decoration: none; color: var(--dodla-text);
    font-size: 14px; font-weight: 500;
    transition: color 0.2s;
  }
  .nav-link:hover { color: var(--dodla-blue); }
  .cart-badge {
    background: var(--dodla-gold); color: white;
    border-radius: 20px; padding: 4px 12px;
    font-size: 13px; font-weight: 600;
    cursor: pointer;
  }

  /* ---- HERO BANNER ---- */
  .hero-banner {
    background: linear-gradient(135deg, #003087 0%, #0055C8 60%, #1a75ff 100%);
    color: white;
    padding: 60px 60px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-radius: 0 0 24px 24px;
    margin-bottom: 32px;
  }
  .hero-text h1 { font-size: 42px; font-weight: 700; line-height: 1.2; margin: 0 0 12px; }
  .hero-text h1 span { color: var(--dodla-gold); }
  .hero-text p { font-size: 16px; opacity: 0.9; margin-bottom: 24px; }
  .hero-btn {
    display: inline-block;
    background: var(--dodla-gold);
    color: white;
    padding: 12px 28px;
    border-radius: 30px;
    font-size: 15px;
    font-weight: 600;
    text-decoration: none;
    cursor: pointer;
  }
  .hero-emoji { font-size: 100px; }

  /* ---- CITY PILL SELECTOR ---- */
  .city-strip {
    background: var(--dodla-light);
    padding: 14px 40px;
    display: flex;
    align-items: center;
    gap: 12px;
    flex-wrap: wrap;
    margin-bottom: 8px;
  }
  .city-label { font-weight: 600; color: var(--dodla-blue); font-size: 14px; margin-right: 6px; }

  /* ---- SECTION HEADER ---- */
  .section-header {
    font-size: 24px;
    font-weight: 700;
    color: var(--dodla-blue);
    margin: 32px 0 4px;
    padding-bottom: 8px;
    border-bottom: 3px solid var(--dodla-gold);
    display: inline-block;
  }
  .section-sub {
    color: #666;
    font-size: 14px;
    margin-bottom: 20px;
  }

  /* ---- PRODUCT CARD ---- */
  .product-card {
    background: white;
    border-radius: 16px;
    padding: 16px;
    text-align: center;
    box-shadow: 0 2px 16px rgba(0,0,0,0.07);
    transition: transform 0.2s, box-shadow 0.2s;
    height: 100%;
    position: relative;
  }
  .product-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 28px rgba(0,0,255,0.12);
  }
  .product-emoji { font-size: 64px; margin: 8px 0; }
  .product-name { font-size: 15px; font-weight: 600; color: var(--dodla-text); margin: 8px 0 4px; }
  .product-desc { font-size: 12px; color: #888; margin-bottom: 10px; min-height: 32px; }
  .price-row { display: flex; align-items: center; justify-content: center; gap: 8px; margin-bottom: 12px; }
  .sale-price { font-size: 18px; font-weight: 700; color: var(--dodla-blue); }
  .original-price { font-size: 13px; color: #aaa; text-decoration: line-through; }
  .sale-badge {
    position: absolute; top: 12px; right: 12px;
    background: #E53E3E; color: white;
    font-size: 11px; font-weight: 700;
    padding: 3px 8px; border-radius: 20px;
  }
  .bestseller-badge {
    position: absolute; top: 12px; left: 12px;
    background: var(--dodla-gold); color: white;
    font-size: 11px; font-weight: 700;
    padding: 3px 8px; border-radius: 20px;
  }
  .add-btn {
    width: 100%;
    background: var(--dodla-blue);
    color: white;
    border: none;
    border-radius: 24px;
    padding: 9px 0;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.2s;
  }
  .add-btn:hover { background: #0041b8; }

  /* ---- CART SIDEBAR ---- */
  .cart-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0;
    border-bottom: 1px solid #eee;
    font-size: 14px;
  }
  .cart-total {
    font-size: 18px; font-weight: 700;
    color: var(--dodla-blue);
    margin-top: 16px;
  }

  /* ---- WHY DODLA STRIP ---- */
  .why-strip {
    background: var(--dodla-blue);
    color: white;
    border-radius: 20px;
    padding: 36px 40px;
    margin: 40px 0;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
    text-align: center;
  }
  .why-item h3 { font-size: 28px; margin: 0; color: var(--dodla-gold); }
  .why-item p { font-size: 13px; margin: 4px 0 0; opacity: 0.9; }

  /* ---- NEWSLETTER ---- */
  .newsletter-box {
    background: var(--dodla-light);
    border-radius: 20px;
    padding: 40px;
    text-align: center;
    margin: 32px 0;
  }
  .newsletter-box h2 { color: var(--dodla-blue); font-size: 26px; margin-bottom: 8px; }
  .newsletter-box p { color: #555; margin-bottom: 24px; }

  /* ---- FOOTER ---- */
  .footer {
    background: var(--dodla-blue);
    color: white;
    padding: 40px;
    margin-top: 40px;
    border-radius: 20px 20px 0 0;
  }
  .footer h4 { color: var(--dodla-gold); font-size: 15px; margin-bottom: 12px; }
  .footer p, .footer a { font-size: 13px; color: rgba(255,255,255,0.8); text-decoration: none; line-height: 2; }
  .footer a:hover { color: var(--dodla-gold); }
  .footer-bottom {
    border-top: 1px solid rgba(255,255,255,0.15);
    margin-top: 28px; padding-top: 16px;
    font-size: 12px; color: rgba(255,255,255,0.5);
    text-align: center;
  }

  /* ---- TOAST ---- */
  .toast {
    background: #22c55e; color: white;
    padding: 10px 20px; border-radius: 30px;
    font-size: 14px; font-weight: 600;
    text-align: center;
  }
</style>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────
# SESSION STATE
# ──────────────────────────────────────────────
if "city" not in st.session_state:
    st.session_state.city = None
if "cart" not in st.session_state:
    st.session_state.cart = {}
if "show_cart" not in st.session_state:
    st.session_state.show_cart = False


# ──────────────────────────────────────────────
# PRODUCT DATA  (city → category → [products])
# ──────────────────────────────────────────────
CITIES = ["Hyderabad", "Bangalore", "Chennai", "Vijayawada", "Tirupati"]

# City-specific prices (slight variation like Provilac)
CITY_PRICE_MULTIPLIER = {
    "Hyderabad":   1.00,
    "Bangalore":   1.05,
    "Chennai":     1.02,
    "Vijayawada":  0.98,
    "Tirupati":    0.97,
}

PRODUCTS = {
    "Fresh Milk": [
        {
            "name": "Full Cream Milk",
            "emoji": "🥛",
            "desc": "Rich & creamy full cream milk, 6% fat. Fresh from farms every morning.",
            "price": 68,
            "original": 75,
            "bestseller": True,
            "sale": True,
        },
        {
            "name": "Standardised Milk",
            "emoji": "🥛",
            "desc": "Standardised cow milk with 4.5% fat. Perfect for everyday use.",
            "price": 52,
            "original": None,
            "bestseller": False,
            "sale": False,
        },
        {
            "name": "Toned Milk",
            "emoji": "🥛",
            "desc": "Light & healthy toned milk with 3% fat. Great for health-conscious families.",
            "price": 44,
            "original": None,
            "bestseller": False,
            "sale": False,
        },
        {
            "name": "Double Toned Milk",
            "emoji": "🥛",
            "desc": "Low-fat double toned milk with 1.5% fat. Ideal for weight management.",
            "price": 40,
            "original": 46,
            "bestseller": False,
            "sale": True,
        },
        {
            "name": "Skimmed Milk",
            "emoji": "🥛",
            "desc": "Fat-free skimmed milk. Perfect for fitness enthusiasts and diabetics.",
            "price": 38,
            "original": None,
            "bestseller": False,
            "sale": False,
        },
    ],
    "UHT Long Life Milk": [
        {
            "name": "UHT Full Cream Milk",
            "emoji": "📦",
            "desc": "Ultra-high temperature processed. Stays fresh 90 days. No boiling needed.",
            "price": 75,
            "original": 85,
            "bestseller": True,
            "sale": True,
        },
        {
            "name": "UHT Toned Milk",
            "emoji": "📦",
            "desc": "Long-life toned milk. Convenient 500 ml Fino pack. Shelf-stable.",
            "price": 32,
            "original": None,
            "bestseller": False,
            "sale": False,
        },
        {
            "name": "UHT Double Toned Milk",
            "emoji": "📦",
            "desc": "Light & long-lasting. Great for travel and emergency stock.",
            "price": 30,
            "original": None,
            "bestseller": False,
            "sale": False,
        },
    ],
    "Curd & Buttermilk": [
        {
            "name": "Fresh Curd – Toned",
            "emoji": "🫙",
            "desc": "Thick, creamy toned curd. Available in pouches, cups & buckets.",
            "price": 55,
            "original": 65,
            "bestseller": True,
            "sale": True,
        },
        {
            "name": "Fresh Curd – Double Toned",
            "emoji": "🫙",
            "desc": "Light and probiotic-rich double toned curd. Great for digestion.",
            "price": 48,
            "original": None,
            "bestseller": False,
            "sale": False,
        },
        {
            "name": "Spiced Buttermilk",
            "emoji": "🥤",
            "desc": "Refreshing buttermilk with a hint of spices. Perfect for summer.",
            "price": 20,
            "original": 25,
            "bestseller": False,
            "sale": True,
        },
        {
            "name": "Plain Buttermilk",
            "emoji": "🥤",
            "desc": "Pure and natural buttermilk. Light on stomach, rich in probiotics.",
            "price": 18,
            "original": None,
            "bestseller": False,
            "sale": False,
        },
    ],
    "Ghee": [
        {
            "name": "Pure Cow Ghee",
            "emoji": "🫙",
            "desc": "Traditional bilona cow ghee. Rich aroma, golden colour, made from cow milk.",
            "price": 584,
            "original": 650,
            "bestseller": True,
            "sale": True,
        },
        {
            "name": "Pure Buffalo Ghee",
            "emoji": "🫙",
            "desc": "Creamy buffalo milk ghee. Dense texture, perfect for sweets & cooking.",
            "price": 636,
            "original": None,
            "bestseller": False,
            "sale": False,
        },
        {
            "name": "High Aroma Ghee",
            "emoji": "✨",
            "desc": "Special high-aroma ghee with intense fragrance. Elevate every meal.",
            "price": 699,
            "original": 799,
            "bestseller": False,
            "sale": True,
        },
    ],
    "Paneer & Sweets": [
        {
            "name": "Fresh Paneer",
            "emoji": "🧀",
            "desc": "Soft, fresh malai paneer made from full-cream milk. 200g block.",
            "price": 90,
            "original": 110,
            "bestseller": True,
            "sale": True,
        },
        {
            "name": "Masala Paneer",
            "emoji": "🧀",
            "desc": "Spice-marinated paneer. Ready to cook. Great for paneer tikka & curries.",
            "price": 110,
            "original": None,
            "bestseller": False,
            "sale": False,
        },
        {
            "name": "Doodh Peda",
            "emoji": "🍬",
            "desc": "Traditional milk sweets made from pure Dodla milk. Melt-in-mouth texture.",
            "price": 120,
            "original": 140,
            "bestseller": False,
            "sale": True,
        },
    ],
    "Flavoured Milk & Lassi": [
        {
            "name": "Chocolate Flavoured Milk",
            "emoji": "🍫",
            "desc": "Rich cocoa milk drink. Kids love it! Packed with calcium & energy.",
            "price": 45,
            "original": 55,
            "bestseller": True,
            "sale": True,
        },
        {
            "name": "Badam Milk",
            "emoji": "🌰",
            "desc": "Almond-infused flavoured milk. Traditional taste with natural goodness.",
            "price": 50,
            "original": None,
            "bestseller": False,
            "sale": False,
        },
        {
            "name": "Rose Lassi",
            "emoji": "🌹",
            "desc": "Creamy rose-flavoured lassi. Made with fresh curd & real rose essence.",
            "price": 35,
            "original": 40,
            "bestseller": False,
            "sale": True,
        },
        {
            "name": "Mango Lassi",
            "emoji": "🥭",
            "desc": "Thick, refreshing mango lassi made with real Alphonso pulp & fresh curd.",
            "price": 40,
            "original": None,
            "bestseller": False,
            "sale": False,
        },
    ],
}

# ──────────────────────────────────────────────
# HELPERS
# ──────────────────────────────────────────────
def city_price(base: int) -> int:
    if st.session_state.city:
        return int(base * CITY_PRICE_MULTIPLIER.get(st.session_state.city, 1.0))
    return base

def add_to_cart(product_name: str, price: int):
    if product_name in st.session_state.cart:
        st.session_state.cart[product_name]["qty"] += 1
    else:
        st.session_state.cart[product_name] = {"qty": 1, "price": price}

def cart_total():
    return sum(v["qty"] * v["price"] for v in st.session_state.cart.values())

def cart_count():
    return sum(v["qty"] for v in st.session_state.cart.values())


# ──────────────────────────────────────────────
# CITY SELECTOR POPUP
# ──────────────────────────────────────────────
if st.session_state.city is None:
    st.markdown("""
    <div style="
      position:fixed; top:0; left:0; width:100%; height:100%;
      background:rgba(0,0,0,0.6); z-index:9999;
      display:flex; align-items:center; justify-content:center;
    ">
      <div style="
        background:white; border-radius:24px; padding:48px 40px;
        max-width:520px; width:90%; text-align:center;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
      ">
        <div style="font-size:56px; margin-bottom:12px;">🥛</div>
        <h2 style="color:#003087; font-size:26px; margin-bottom:8px;">Welcome to Dodla Dairy</h2>
        <p style="color:#555; font-size:15px; margin-bottom:28px;">
          Pure milk, straight from our farms to your doorstep.<br/>
          <strong>Please select your city to get started.</strong>
        </p>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br><br><br><br><br>", unsafe_allow_html=True)
    st.markdown(
        "<h2 style='text-align:center;color:#003087;'>📍 Select Your City</h2>"
        "<p style='text-align:center;color:#555;'>We deliver fresh dairy products across South India</p>",
        unsafe_allow_html=True
    )

    city_emojis = {"Hyderabad": "🏙️", "Bangalore": "🌆", "Chennai": "🌊",
                   "Vijayawada": "🕌", "Tirupati": "⛩️"}

    cols = st.columns(len(CITIES))
    for i, city in enumerate(CITIES):
        with cols[i]:
            if st.button(f"{city_emojis[city]}\n{city}", key=f"city_{city}",
                         use_container_width=True):
                st.session_state.city = city
                st.rerun()
    st.stop()


# ──────────────────────────────────────────────
# TOP ANNOUNCEMENT BAR
# ──────────────────────────────────────────────
st.markdown(
    f'<div class="topbar">🚚 FREE delivery on orders above ₹299 | '
    f'Now delivering in <strong>{st.session_state.city}</strong> 🥛 '
    f'Established 1995 • ISO 22000 Certified</div>',
    unsafe_allow_html=True
)

# ──────────────────────────────────────────────
# NAVBAR
# ──────────────────────────────────────────────
n1, n2, n3, n4 = st.columns([2, 3, 2, 1])
with n1:
    st.markdown(
        '<div class="navbar-logo">Dodla <span>Dairy</span> 🥛</div>',
        unsafe_allow_html=True
    )
with n2:
    search_query = st.text_input("", placeholder="🔍  Search products…", label_visibility="collapsed")
with n3:
    city_options = ["📍 " + c for c in CITIES]
    current_idx = CITIES.index(st.session_state.city) if st.session_state.city in CITIES else 0
    chosen = st.selectbox("City", city_options, index=current_idx, label_visibility="collapsed")
    new_city = chosen.replace("📍 ", "")
    if new_city != st.session_state.city:
        st.session_state.city = new_city
        st.rerun()
with n4:
    if st.button(f"🛒  Cart ({cart_count()})", use_container_width=True):
        st.session_state.show_cart = not st.session_state.show_cart

st.markdown("<hr style='margin:0;border-color:#eee;'>", unsafe_allow_html=True)


# ──────────────────────────────────────────────
# CART PANEL
# ──────────────────────────────────────────────
if st.session_state.show_cart:
    with st.container():
        st.markdown("### 🛒 Your Cart")
        if not st.session_state.cart:
            st.info("Your cart is empty. Add some products!")
        else:
            for prod_name, details in list(st.session_state.cart.items()):
                c1, c2, c3, c4 = st.columns([3, 1, 1, 1])
                c1.write(f"**{prod_name}**")
                c2.write(f"₹{details['price']}")
                new_qty = c3.number_input("Qty", min_value=0, max_value=20,
                                          value=details["qty"],
                                          key=f"qty_{prod_name}",
                                          label_visibility="collapsed")
                if new_qty == 0:
                    del st.session_state.cart[prod_name]
                    st.rerun()
                else:
                    st.session_state.cart[prod_name]["qty"] = new_qty
                c4.write(f"₹{details['price'] * details['qty']}")

            st.markdown(f"<div class='cart-total'>Total: ₹{cart_total()}</div>", unsafe_allow_html=True)
            col_a, col_b = st.columns(2)
            with col_a:
                if st.button("🗑️ Clear Cart", use_container_width=True):
                    st.session_state.cart = {}
                    st.rerun()
            with col_b:
                if st.button("✅ Checkout", type="primary", use_container_width=True):
                    st.success("🎉 Order placed! Our team will contact you shortly.")
                    st.session_state.cart = {}
        st.markdown("<hr>", unsafe_allow_html=True)


# ──────────────────────────────────────────────
# HERO BANNER
# ──────────────────────────────────────────────
st.markdown(f"""
<div class="hero-banner
