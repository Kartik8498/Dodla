import streamlit as st

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
# PREMIUM THEME / STYLES
# --------------------------------------------------
st.markdown(
    """
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

      html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
        background: #fffdfd;
        color: #1d1b1b;
      }

      :root{
        --bg: #fffdfd;
        --surface: #ffffff;
        --surface-2: #fff7f7;
        --line: rgba(224, 60, 72, 0.12);
        --text: #1d1b1b;
        --muted: #6f6767;
        --red: #e53e4d;
        --red-2: #ff6b78;
        --red-3: #ffedf0;
        --shadow: 0 18px 50px rgba(92, 20, 27, 0.08);
        --shadow-soft: 0 8px 24px rgba(92, 20, 27, 0.06);
        --radius-xl: 30px;
        --radius-lg: 22px;
        --radius-md: 18px;
      }

      .block-container{
        padding-top: 0.5rem;
        padding-bottom: 2rem;
        max-width: 1400px;
      }

      #MainMenu, footer, header { visibility: hidden; }

      .topbar {
        background: linear-gradient(90deg, #fff5f5, #ffecee);
        color: var(--red);
        border: 1px solid rgba(229, 62, 77, 0.14);
        text-align: center;
        padding: 10px 16px;
        border-radius: 0 0 18px 18px;
        font-size: 13px;
        font-weight: 600;
        letter-spacing: 0.2px;
        margin-bottom: 12px;
      }

      .navbar-shell {
        position: sticky;
        top: 8px;
        z-index: 999;
        background: rgba(255,255,255,0.78);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(229, 62, 77, 0.10);
        border-radius: 22px;
        padding: 14px 16px;
        box-shadow: var(--shadow-soft);
        margin-bottom: 18px;
      }

      .brand {
        font-size: 24px;
        font-weight: 800;
        letter-spacing: -0.5px;
        color: var(--text);
        line-height: 1;
        white-space: nowrap;
      }
      .brand span { color: var(--red); }

      .hero {
        background:
          radial-gradient(circle at top right, rgba(255,255,255,0.20), transparent 28%),
          linear-gradient(135deg, #fff7f8 0%, #fff1f3 45%, #ffe7ea 100%);
        border: 1px solid rgba(229, 62, 77, 0.10);
        border-radius: 34px;
        padding: 34px;
        box-shadow: var(--shadow);
        margin: 6px 0 24px;
        overflow: hidden;
      }

      .hero-grid {
        display: grid;
        grid-template-columns: 1.25fr 0.75fr;
        gap: 24px;
        align-items: center;
      }

      .eyebrow {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 9px 14px;
        background: rgba(229, 62, 77, 0.08);
        border: 1px solid rgba(229, 62, 77, 0.12);
        color: var(--red);
        border-radius: 999px;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.2px;
      }

      .hero h1 {
        font-size: 54px;
        line-height: 1.02;
        margin: 14px 0 12px;
        font-weight: 800;
        letter-spacing: -1.5px;
        color: var(--text);
      }
      .hero h1 span { color: var(--red); }

      .hero p {
        font-size: 16px;
        line-height: 1.75;
        margin: 0 0 18px;
        color: var(--muted);
        max-width: 720px;
      }

      .hero-actions {
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
        margin: 12px 0 0;
      }

      .pill {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 10px 14px;
        border-radius: 999px;
        background: #fff;
        border: 1px solid var(--line);
        color: var(--text);
        font-size: 13px;
        font-weight: 600;
        box-shadow: 0 8px 18px rgba(0,0,0,0.03);
      }

      .hero-panel {
        background: linear-gradient(180deg, #ffffff, #fff9f9);
        border: 1px solid rgba(229, 62, 77, 0.10);
        border-radius: 30px;
        padding: 24px;
        box-shadow: 0 14px 30px rgba(92, 20, 27, 0.06);
        text-align: center;
      }

      .hero-emoji {
        font-size: 88px;
        line-height: 1;
        margin-bottom: 12px;
      }

      .hero-metrics {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 10px;
        margin-top: 18px;
      }

      .metric {
        background: #fff;
        border: 1px solid var(--line);
        border-radius: 18px;
        padding: 14px 8px;
      }
      .metric h3 {
        margin: 0;
        font-size: 18px;
        color: var(--red);
      }
      .metric p {
        margin: 4px 0 0;
        color: var(--muted);
        font-size: 12px;
        line-height: 1.4;
      }

      .section-title {
        font-size: 24px;
        font-weight: 800;
        color: var(--text);
        letter-spacing: -0.5px;
        margin: 12px 0 3px;
      }
      .section-title span { color: var(--red); }
      .section-subtitle {
        color: var(--muted);
        font-size: 14px;
        margin-bottom: 14px;
      }

      .grid-3, .grid-4, .grid-5 {
        display: grid;
        gap: 16px;
      }
      .grid-3 { grid-template-columns: repeat(3, 1fr); }
      .grid-4 { grid-template-columns: repeat(4, 1fr); }
      .grid-5 { grid-template-columns: repeat(5, 1fr); }

      .card {
        background: var(--surface);
        border: 1px solid rgba(229, 62, 77, 0.10);
        border-radius: var(--radius-lg);
        box-shadow: var(--shadow-soft);
        padding: 18px;
        height: 100%;
      }

      .promo-card {
        min-height: 154px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        background: linear-gradient(180deg, #fff, #fff7f8);
      }

      .promo-label {
        display: inline-flex;
        width: fit-content;
        align-items: center;
        padding: 7px 12px;
        border-radius: 999px;
        background: var(--red-3);
        color: var(--red);
        font-size: 12px;
        font-weight: 700;
        margin-bottom: 10px;
      }

      .promo-card h3, .feature-card h3, .product-card h4, .form-card h3 {
        margin: 0 0 6px;
        color: var(--text);
        letter-spacing: -0.2px;
      }

      .promo-card p, .feature-card p, .product-card p {
        margin: 0;
        color: var(--muted);
        font-size: 13px;
        line-height: 1.65;
      }

      .promo-emoji {
        font-size: 48px;
        line-height: 1;
        text-align: right;
      }

      .category-pill {
        background: #fff;
        border: 1px solid rgba(229, 62, 77, 0.10);
        border-radius: 18px;
        padding: 16px 12px;
        text-align: center;
        box-shadow: 0 8px 20px rgba(0,0,0,0.03);
        font-weight: 700;
        color: var(--text);
        font-size: 13px;
      }

      .product-card {
        position: relative;
        overflow: hidden;
        background:
          linear-gradient(180deg, rgba(255,255,255,0.98), rgba(255,249,249,0.98));
      }

      .badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        font-size: 11px;
        font-weight: 800;
        padding: 5px 10px;
        border-radius: 999px;
        margin-right: 6px;
        margin-bottom: 10px;
      }
      .badge.best { background: #fff1c8; color: #946200; }
      .badge.sale { background: #ffe2e6; color: #bb1d33; }

      .product-emoji {
        font-size: 58px;
        line-height: 1;
        margin: 10px 0 12px;
      }

      .price-row {
        display: flex;
        align-items: center;
        gap: 10px;
        flex-wrap: wrap;
        margin: 10px 0 14px;
      }
      .sale-price {
        font-size: 21px;
        font-weight: 800;
        color: var(--red);
      }
      .original-price {
        font-size: 13px;
        color: #9c8f90;
        text-decoration: line-through;
      }
      .small {
        font-size: 12px;
        color: var(--muted);
      }

      .section-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(229,62,77,0.18), transparent);
        margin: 18px 0;
      }

      .cart-card {
        background: linear-gradient(180deg, #fff, #fff8f9);
        border: 1px solid rgba(229, 62, 77, 0.10);
        border-radius: 24px;
        padding: 18px;
        box-shadow: var(--shadow-soft);
      }

      .cart-total {
        font-size: 18px;
        font-weight: 800;
        color: var(--red);
        margin-top: 14px;
      }

      .trust-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 16px;
      }

      .trust-item {
        background: #fff;
        border: 1px solid rgba(229, 62, 77, 0.10);
        border-radius: 20px;
        padding: 18px;
        box-shadow: var(--shadow-soft);
      }

      .trust-item .icon {
        font-size: 28px;
        margin-bottom: 10px;
      }

      .trust-item h4 {
        margin: 0 0 6px;
        color: var(--text);
      }
      .trust-item p {
        margin: 0;
        color: var(--muted);
        font-size: 13px;
        line-height: 1.65;
      }

      .testimonial {
        background: linear-gradient(180deg, #fff, #fff7f8);
        border: 1px solid rgba(229, 62, 77, 0.10);
        border-radius: 22px;
        padding: 18px;
        box-shadow: var(--shadow-soft);
      }
      .testimonial .stars { color: #f4b400; font-size: 18px; letter-spacing: 1px; }
      .testimonial p { color: var(--text); line-height: 1.8; font-size: 14px; }

      .faq-box {
        background: #fff;
        border: 1px solid rgba(229, 62, 77, 0.10);
        border-radius: 18px;
        margin-bottom: 10px;
        box-shadow: var(--shadow-soft);
        overflow: hidden;
      }

      .footer {
        margin-top: 30px;
        background: linear-gradient(135deg, #2b0e13, #7b1523);
        color: white;
        border-radius: 28px;
        padding: 28px;
        box-shadow: 0 24px 60px rgba(43, 14, 19, 0.18);
      }
      .footer h4 {
        color: #ffd0d7;
        margin: 0 0 10px;
      }
      .footer p, .footer a {
        color: rgba(255,255,255,0.88);
        font-size: 13px;
        line-height: 1.85;
        text-decoration: none;
      }

      .stButton > button {
        border-radius: 999px !important;
        border: 1px solid rgba(229, 62, 77, 0.16) !important;
        background: linear-gradient(135deg, var(--red), #ff5f71) !important;
        color: white !important;
        font-weight: 700 !important;
        padding: 0.68rem 1rem !important;
        box-shadow: 0 12px 24px rgba(229, 62, 77, 0.20) !important;
        transition: transform .18s ease, box-shadow .18s ease !important;
      }
      .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 16px 30px rgba(229, 62, 77, 0.24) !important;
      }

      .stTextInput > div > div > input,
      .stSelectbox > div > div,
      .stTextArea textarea {
        border-radius: 16px !important;
        border: 1px solid rgba(229, 62, 77, 0.12) !important;
        background: #fff !important;
      }

      @media (max-width: 900px) {
        .hero-grid, .grid-3, .grid-4, .grid-5, .trust-grid {
          grid-template-columns: 1fr;
        }
        .hero h1 { font-size: 36px; }
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "city" not in st.session_state:
    st.session_state.city = None
if "cart" not in st.session_state:
    st.session_state.cart = {}
if "show_cart" not in st.session_state:
    st.session_state.show_cart = False

# --------------------------------------------------
# DATA
# --------------------------------------------------
CITIES = ["Hyderabad", "Bangalore", "Chennai", "Vijayawada", "Tirupati"]

CITY_PRICE_MULTIPLIER = {
    "Hyderabad": 1.00,
    "Bangalore": 1.05,
    "Chennai": 1.02,
    "Vijayawada": 0.98,
    "Tirupati": 0.97,
}

PRODUCTS = {
    "Fresh Milk": [
        {"name": "Full Cream Milk", "emoji": "🥛", "desc": "Rich and creamy full cream milk, fresh every morning.", "price": 68, "original": 75, "bestseller": True, "sale": True},
        {"name": "Standardised Milk", "emoji": "🥛", "desc": "Perfect everyday milk with balanced taste and nutrition.", "price": 52, "original": None, "bestseller": False, "sale": False},
        {"name": "Toned Milk", "emoji": "🥛", "desc": "Light and healthy choice for family consumption.", "price": 44, "original": None, "bestseller": False, "sale": False},
        {"name": "Double Toned Milk", "emoji": "🥛", "desc": "Low-fat milk for a lighter daily routine.", "price": 40, "original": 46, "bestseller": False, "sale": True},
    ],
    "UHT Long Life Milk": [
        {"name": "UHT Full Cream Milk", "emoji": "📦", "desc": "Long-life milk with convenience and freshness.", "price": 75, "original": 85, "bestseller": True, "sale": True},
        {"name": "UHT Toned Milk", "emoji": "📦", "desc": "Shelf-stable toned milk for easy storage.", "price": 32, "original": None, "bestseller": False, "sale": False},
        {"name": "UHT Double Toned Milk", "emoji": "📦", "desc": "Light, long-lasting, and travel-friendly.", "price": 30, "original": None, "bestseller": False, "sale": False},
    ],
    "Curd & Buttermilk": [
        {"name": "Fresh Curd – Toned", "emoji": "🫙", "desc": "Thick, creamy curd in a premium pack.", "price": 55, "original": 65, "bestseller": True, "sale": True},
        {"name": "Spiced Buttermilk", "emoji": "🥤", "desc": "Refreshing buttermilk with a subtle spice finish.", "price": 20, "original": 25, "bestseller": False, "sale": True},
        {"name": "Plain Buttermilk", "emoji": "🥤", "desc": "Simple, natural, and probiotic rich.", "price": 18, "original": None, "bestseller": False, "sale": False},
    ],
    "Ghee": [
        {"name": "Pure Cow Ghee", "emoji": "🫙", "desc": "Traditional golden ghee with rich aroma.", "price": 584, "original": 650, "bestseller": True, "sale": True},
        {"name": "Pure Buffalo Ghee", "emoji": "🫙", "desc": "Dense and creamy ghee for cooking and sweets.", "price": 636, "original": None, "bestseller": False, "sale": False},
        {"name": "High Aroma Ghee", "emoji": "✨", "desc": "Premium fragrance for special meals.", "price": 699, "original": 799, "bestseller": False, "sale": True},
    ],
    "Paneer & Sweets": [
        {"name": "Fresh Paneer", "emoji": "🧀", "desc": "Soft malai paneer made from full-cream milk.", "price": 90, "original": 110, "bestseller": True, "sale": True},
        {"name": "Masala Paneer", "emoji": "🧀", "desc": "Ready-to-cook paneer with a spice coating.", "price": 110, "original": None, "bestseller": False, "sale": False},
        {"name": "Doodh Peda", "emoji": "🍬", "desc": "Traditional milk sweet with a melt-in-mouth finish.", "price": 120, "original": 140, "bestseller": False, "sale": True},
    ],
    "Flavoured Milk & Lassi": [
        {"name": "Chocolate Flavoured Milk", "emoji": "🍫", "desc": "Cocoa-rich milk drink loved by kids.", "price": 45, "original": 55, "bestseller": True, "sale": True},
        {"name": "Badam Milk", "emoji": "🌰", "desc": "Almond-infused drink with a classic taste.", "price": 50, "original": None, "bestseller": False, "sale": False},
        {"name": "Rose Lassi", "emoji": "🌹", "desc": "Creamy rose lassi with fresh curd and fragrance.", "price": 35, "original": 40, "bestseller": False, "sale": True},
        {"name": "Mango Lassi", "emoji": "🥭", "desc": "Thick lassi made with real mango pulp.", "price": 40, "original": None, "bestseller": False, "sale": False},
    ],
}

FAQS = [
    ("How do I place an order?", "Choose your city, add products to cart, and checkout from the cart panel."),
    ("Can this become a real store?", "Yes. Add payment, database, order tracking, and subscription scheduling."),
    ("Which cities are supported?", "Hyderabad, Bangalore, Chennai, Vijayawada, and Tirupati are enabled in this demo."),
]

CATEGORY_ORDER = list(PRODUCTS.keys())
CATEGORY_ICON = {
    "Fresh Milk": "🥛",
    "UHT Long Life Milk": "📦",
    "Curd & Buttermilk": "🫙",
    "Ghee": "✨",
    "Paneer & Sweets": "🧀",
    "Flavoured Milk & Lassi": "🍫",
}

# --------------------------------------------------
# HELPERS
# --------------------------------------------------
def city_price(base: int) -> int:
    if st.session_state.city:
        return int(base * CITY_PRICE_MULTIPLIER.get(st.session_state.city, 1.0))
    return base


def add_to_cart(product_name: str, price: int):
    if product_name in st.session_state.cart:
        st.session_state.cart[product_name]["qty"] += 1
    else:
        st.session_state.cart[product_name] = {"qty": 1, "price": price}


def cart_total() -> int:
    return sum(v["qty"] * v["price"] for v in st.session_state.cart.values())


def cart_count() -> int:
    return sum(v["qty"] for v in st.session_state.cart.values())


def all_products():
    items = []
    for category, plist in PRODUCTS.items():
        for product in plist:
            items.append((category, product))
    return items


def render_title(title: str, subtitle: str = ""):
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)
    if subtitle:
        st.markdown(f'<div class="section-subtitle">{subtitle}</div>', unsafe_allow_html=True)


# --------------------------------------------------
# CITY PICKER
# --------------------------------------------------
if st.session_state.city is None:
    st.markdown(
        """
        <div class="hero">
          <div class="hero-grid">
            <div>
              <div class="eyebrow">🥛 Premium dairy shopping experience</div>
              <h1>Welcome to <span>Dodla Dairy</span></h1>
              <p>
                Select your city to browse a premium storefront for milk, curd, paneer, ghee,
                and flavoured dairy products.
              </p>
              <div class="hero-actions">
                <div class="pill">🚚 Free delivery above ₹299</div>
                <div class="pill">⭐ Fresh premium quality</div>
                <div class="pill">📦 Subscription ready</div>
              </div>
            </div>
            <div class="hero-panel">
              <div class="hero-emoji">🐄</div>
              <h3 style="margin:0 0 8px;">Choose your city</h3>
              <p style="margin:0; color:var(--muted); line-height:1.7;">
                We deliver fresh dairy products across South India.
              </p>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns(len(CITIES))
    city_emojis = {"Hyderabad": "🏙️", "Bangalore": "🌆", "Chennai": "🌊", "Vijayawada": "🕌", "Tirupati": "⛩️"}
    for i, city in enumerate(CITIES):
        with cols[i]:
            if st.button(f"{city_emojis[city]}\n{city}", key=f"city_{city}", use_container_width=True):
                st.session_state.city = city
                st.rerun()
    st.stop()

# --------------------------------------------------
# TOP BAR
# --------------------------------------------------
st.markdown(
    f'<div class="topbar">🚚 Free delivery on orders above ₹299 | Delivering in <strong>{st.session_state.city}</strong> | Fresh dairy since 1995</div>',
    unsafe_allow_html=True,
)

# --------------------------------------------------
# NAVBAR
# --------------------------------------------------
st.markdown('<div class="navbar-shell">', unsafe_allow_html=True)
n1, n2, n3, n4 = st.columns([1.1, 2.8, 1.2, 0.8])
with n1:
    st.markdown('<div class="brand">Dodla <span>Dairy</span> 🥛</div>', unsafe_allow_html=True)
with n2:
    search_query = st.text_input(
        "",
        placeholder="Search products, categories, or favorites…",
        label_visibility="collapsed",
    )
with n3:
    chosen = st.selectbox("City", [f"📍 {c}" for c in CITIES], index=CITIES.index(st.session_state.city), label_visibility="collapsed")
    new_city = chosen.replace("📍 ", "")
    if new_city != st.session_state.city:
        st.session_state.city = new_city
        st.rerun()
with n4:
    if st.button(f"🛒 {cart_count()}", use_container_width=True):
        st.session_state.show_cart = not st.session_state.show_cart
st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------------------------
# HERO
# --------------------------------------------------
st.markdown(
    f"""
    <div class="hero">
      <div class="hero-grid">
        <div>
          <div class="eyebrow">✨ White & red premium storefront</div>
          <h1>Fresh dairy delivered <span>beautifully</span></h1>
          <p>
            A polished, premium homepage for Dodla with elegant cards, soft shadows, rich spacing,
            and a warm red identity.
          </p>
          <div class="hero-actions">
            <div class="pill">🕗 Morning delivery slots</div>
            <div class="pill">⭐ Premium curated range</div>
            <div class="pill">🚚 Fast city delivery</div>
          </div>
        </div>
        <div class="hero-panel">
          <div class="hero-emoji">❤️🥛</div>
          <h3 style="margin:0 0 8px;">Farm fresh daily</h3>
          <p style="margin:0; color:var(--muted); line-height:1.7;">
            Premium quality, elegant packaging, and a simple shopping flow.
          </p>
          <div class="hero-metrics">
            <div class="metric"><h3>24h</h3><p>fresh feel</p></div>
            <div class="metric"><h3>5</h3><p>cities</p></div>
            <div class="metric"><h3>100%</h3><p>care</p></div>
          </div>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# OFFERS
# --------------------------------------------------
render_title("Special offers", "Premium promotional cards that make the homepage feel polished.")
promo_cols = st.columns(3)
promos = [
    ("Morning milk plan", "Start a recurring delivery subscription.", "🕗"),
    ("Family pack savings", "Buy more and save on essentials.", "🎁"),
    ("Paneer for dinner", "Fresh paneer for quick meals.", "🧀"),
]
for col, (title, desc, emoji) in zip(promo_cols, promos):
    with col:
        st.markdown(
            f"""
            <div class="card promo-card">
              <div>
                <div class="promo-label">Featured</div>
                <h3>{title}</h3>
                <p>{desc}</p>
              </div>
              <div class="promo-emoji">{emoji}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# --------------------------------------------------
# CATEGORIES
# --------------------------------------------------
render_title("Shop by category", "Neat category tiles with a luxury ecommerce feel.")
cat_cols = st.columns(5)
for idx, cat in enumerate(CATEGORY_ORDER):
    with cat_cols[idx % 5]:
        st.markdown(
            f"""
            <div class="category-pill">
              <div style="font-size:28px; margin-bottom:8px;">{CATEGORY_ICON.get(cat, '🥛')}</div>
              {cat}
            </div>
            """,
            unsafe_allow_html=True,
        )

# --------------------------------------------------
# SHOP + CART
# --------------------------------------------------
shop_col, cart_col = st.columns([2.2, 1])

with shop_col:
    if search_query:
        q = search_query.lower().strip()
        items = [(cat, p) for cat, p in all_products() if q in p["name"].lower() or q in cat.lower()]
        render_title("Search results", f"Matching products for “{search_query}”.")
    else:
        items = all_products()
        render_title("Best sellers & daily essentials", "A premium product grid with city-aware pricing and elegant add-to-cart actions.")

    if not items:
        st.info("No products matched your search.")
    else:
        for i in range(0, len(items), 3):
            row = items[i:i+3]
            cols = st.columns(3)
            for col, (category, product) in zip(cols, row):
                with col:
                    price = city_price(product["price"])
                    original = city_price(product["original"]) if product["original"] else None

                    badges = ""
                    if product["bestseller"]:
                        badges += '<span class="badge best">Best seller</span>'
                    if product["sale"]:
                        badges += '<span class="badge sale">Sale</span>'

                    st.markdown(
                        f"""
                        <div class="card product-card">
                          {badges}
                          <div class="product-emoji">{product['emoji']}</div>
                          <h4>{product['name']}</h4>
                          <div class="small">{category}</div>
                          <p style="margin-top:8px;">{product['desc']}</p>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                    price_html = f"<div class='sale-price'>₹{price}</div>"
                    if original:
                        price_html += f"<div class='original-price'>₹{original}</div>"

                    st.markdown(f"<div class='price-row'>{price_html}</div>", unsafe_allow_html=True)

                    if st.button(f"Add to cart — {product['name']}", key=f"add_{category}_{product['name']}", use_container_width=True):
                        add_to_cart(product["name"], price)
                        st.toast(f"Added {product['name']} to cart")
                        st.rerun()

with cart_col:
    st.markdown(
        f"""
        <div class="cart-card">
          <div style="display:flex; justify-content:space-between; align-items:center; gap:10px;">
            <div>
              <div style="font-size:18px; font-weight:800; color:var(--text);">🛒 Cart</div>
              <div class="small">{cart_count()} item(s)</div>
            </div>
            <div style="font-size:28px;">🧺</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not st.session_state.cart:
        st.info("Your cart is empty. Add products from the shop.")
    else:
        for prod_name, details in list(st.session_state.cart.items()):
            c1, c2 = st.columns([2.2, 1])
            with c1:
                st.write(f"**{prod_name}**")
                st.caption(f"₹{details['price']} each")
            with c2:
                new_qty = st.number_input(
                    "Qty",
                    min_value=0,
                    max_value=20,
                    value=int(details["qty"]),
                    key=f"qty_{prod_name}",
                    label_visibility="collapsed",
                )
                if new_qty == 0:
                    del st.session_state.cart[prod_name]
                    st.rerun()
                st.session_state.cart[prod_name]["qty"] = int(new_qty)
            st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

        st.markdown(f"<div class='cart-total'>Total: ₹{cart_total()}</div>", unsafe_allow_html=True)
        st.caption("Checkout is demo-only here. Connect a payment gateway for live orders.")
        if st.button("Checkout", type="primary", use_container_width=True):
            st.success("Order placed! Connect payments and backend next.")
            st.session_state.cart = {}
            st.rerun()

# --------------------------------------------------
# TRUST / WHY
# --------------------------------------------------
render_title("Why choose Dodla", "A premium trust block for a more elevated homepage.")
trust_cols = st.columns(4)
trust_data = [
    ("🏭", "Farm fresh", "Milk sourced and packaged for freshness."),
    ("🚚", "Fast delivery", "City-wise delivery experience built in."),
    ("🧾", "Easy ordering", "Simple cart and checkout flow."),
    ("⭐", "Premium quality", "Carefully curated dairy essentials."),
]
for col, (icon, title, desc) in zip(trust_cols, trust_data):
    with col:
        st.markdown(
            f"""
            <div class="trust-item">
              <div class="icon">{icon}</div>
              <h4>{title}</h4>
              <p>{desc}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# --------------------------------------------------
# TESTIMONIALS
# --------------------------------------------------
render_title("What customers say", "A soft social-proof section that adds a premium feel.")
review_cols = st.columns(3)
TESTIMONIALS = [
    {"name": "Priya S.", "text": "Very elegant layout. It looks like a real premium dairy brand."},
    {"name": "Ravi K.", "text": "The white and red theme feels polished and modern."},
    {"name": "Anjali M.", "text": "Beautiful product cards and a clean shopping flow."},
]
for col, review in zip(review_cols, TESTIMONIALS):
    with col:
        st.markdown(
            f"""
            <div class="testimonial">
              <div class="stars">★★★★★</div>
              <p>“{review['text']}”</p>
              <div style="font-weight:700; color:var(--red);">{review['name']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# --------------------------------------------------
# SAMPLE / SUBSCRIPTION FORM
# --------------------------------------------------
render_title("Request a sample / subscribe", "Capture leads with a premium-looking form.")
left, right = st.columns([1.2, 1])

with left:
    with st.form("sample_form"):
        name = st.text_input("Full name")
        mobile = st.text_input("Mobile number")
        city = st.selectbox("City", CITIES, index=CITIES.index(st.session_state.city))
        product = st.selectbox("Product", [p["name"] for _, p in all_products()])
        note = st.text_area("Delivery notes", placeholder="Apartment, landmark, preferred time, etc.")
        submitted = st.form_submit_button("Request sample / subscribe")
        if submitted:
            st.success(f"Thanks {name or 'there'} — your request for {product} in {city} is noted.")

with right:
    st.markdown(
        """
        <div class="form-card card">
          <h3>Premium delivery experience</h3>
          <p>
            This section is ideal for lead capture, sample requests, and subscription signups.
            It keeps the page feeling like a real premium ecommerce storefront.
          </p>
          <div class="section-divider"></div>
          <p class="small">
            Next step: connect this form to email, CRM, database, and a payment gateway.
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# --------------------------------------------------
# FAQ
# --------------------------------------------------
render_title("Frequently asked questions", "Clean expandable answers for a premium user experience.")
FAQS = [
    ("How do I place an order?", "Choose your city, add products to cart, and checkout from the cart panel."),
    ("Can this become a real store?", "Yes. Add payment, database, order tracking, and subscription scheduling."),
    ("Which cities are supported?", "Hyderabad, Bangalore, Chennai, Vijayawada, and Tirupati are enabled in this demo."),
]
for question, answer in FAQS:
    with st.expander(question):
        st.write(answer)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown(
    f"""
    <div class="footer">
      <div class="grid-4">
        <div>
          <h4>Dodla Dairy</h4>
          <p>Premium dairy shopping in a clean white and red aesthetic.</p>
        </div>
        <div>
          <h4>Shop</h4>
          <p>Milk<br/>Curd<br/>Paneer<br/>Ghee</p>
        </div>
        <div>
          <h4>Support</h4>
          <p>FAQs<br/>Delivery<br/>Orders<br/>Contact</p>
        </div>
        <div>
          <h4>Contact</h4>
          <p>hello@dodla.com<br/>+91 00000 00000<br/>Delivering in {st.session_state.city}</p>
        </div>
      </div>
      <div class="section-divider" style="background: rgba(255,255,255,0.18);"></div>
      <div style="text-align:center; font-size:13px; opacity:0.9;">© 2026 Dodla Dairy • White & red premium experience</div>
    </div>
    """,
    unsafe_allow_html=True,
)
