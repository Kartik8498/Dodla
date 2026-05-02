import streamlit as st

st.set_page_config(
    page_title="Dodla Dairy",
    page_icon="🥛",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# THEME / STYLE
# -----------------------------
st.markdown(
    """
<style>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

  html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
  }

  :root {
    --dodla-blue: #003087;
    --dodla-blue-2: #0055c8;
    --dodla-gold: #f5a623;
    --dodla-bg: #f6f8fc;
    --dodla-text: #172033;
    --muted: #6d7485;
    --card: #ffffff;
    --line: rgba(10, 24, 58, 0.08);
  }

  .block-container {
    padding-top: 0.5rem;
    padding-bottom: 2rem;
  }

  #MainMenu, footer, header { visibility: hidden; }

  .topbar {
    background: linear-gradient(90deg, var(--dodla-blue), var(--dodla-blue-2));
    color: white;
    text-align: center;
    padding: 8px 12px;
    font-size: 13px;
    letter-spacing: 0.2px;
    border-radius: 0 0 16px 16px;
    margin-bottom: 10px;
  }

  .navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    padding: 14px 18px;
    background: rgba(255,255,255,0.92);
    backdrop-filter: blur(8px);
    border: 1px solid var(--line);
    border-radius: 18px;
    box-shadow: 0 10px 30px rgba(16, 24, 40, 0.06);
    position: sticky;
    top: 8px;
    z-index: 999;
    margin-bottom: 16px;
  }

  .brand {
    font-size: 24px;
    font-weight: 800;
    color: var(--dodla-blue);
    line-height: 1;
    white-space: nowrap;
  }

  .brand span { color: var(--dodla-gold); }

  .nav-links {
    display: flex;
    align-items: center;
    gap: 14px;
    flex-wrap: wrap;
    justify-content: center;
  }

  .nav-link {
    color: var(--dodla-text);
    text-decoration: none;
    font-size: 13px;
    font-weight: 600;
    padding: 8px 10px;
    border-radius: 999px;
    background: rgba(0,48,135,0.04);
  }

  .hero {
    background: linear-gradient(135deg, var(--dodla-blue) 0%, #0e4cb8 55%, #1b7bff 100%);
    border-radius: 28px;
    color: white;
    padding: 36px 34px;
    box-shadow: 0 20px 48px rgba(0,48,135,0.22);
    margin: 8px 0 24px;
    overflow: hidden;
  }

  .hero-grid {
    display: grid;
    grid-template-columns: 1.2fr 0.8fr;
    gap: 24px;
    align-items: center;
  }

  .hero h1 {
    font-size: 46px;
    line-height: 1.05;
    margin: 0 0 12px;
    font-weight: 800;
  }

  .hero h1 span { color: var(--dodla-gold); }

  .hero p {
    font-size: 16px;
    line-height: 1.65;
    margin: 0 0 18px;
    opacity: 0.95;
    max-width: 700px;
  }

  .hero-actions {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
    margin-top: 8px;
  }

  .pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 10px 14px;
    border-radius: 999px;
    background: rgba(255,255,255,0.14);
    border: 1px solid rgba(255,255,255,0.16);
    font-size: 13px;
    font-weight: 600;
    margin-right: 8px;
    margin-top: 8px;
  }

  .hero-card {
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.16);
    border-radius: 24px;
    padding: 20px;
    text-align: center;
  }

  .hero-emoji {
    font-size: 88px;
    line-height: 1;
    margin-bottom: 10px;
  }

  .hero-mini {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin-top: 16px;
  }

  .mini-stat {
    background: rgba(255,255,255,0.1);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 18px;
    padding: 14px 10px;
    text-align: center;
  }

  .mini-stat h3 {
    margin: 0;
    font-size: 18px;
    color: #fff;
  }

  .mini-stat p {
    margin: 4px 0 0;
    font-size: 12px;
    opacity: 0.9;
  }

  .section-title {
    font-size: 24px;
    font-weight: 800;
    color: var(--dodla-blue);
    margin: 10px 0 2px;
  }

  .section-subtitle {
    color: var(--muted);
    font-size: 14px;
    margin-bottom: 14px;
  }

  .promo-grid, .info-grid, .testimonial-grid, .category-grid {
    display: grid;
    gap: 16px;
  }

  .promo-grid { grid-template-columns: repeat(3, 1fr); }
  .info-grid { grid-template-columns: repeat(4, 1fr); }
  .testimonial-grid { grid-template-columns: repeat(3, 1fr); }
  .category-grid { grid-template-columns: repeat(5, 1fr); }

  .card {
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 20px;
    box-shadow: 0 10px 24px rgba(18, 31, 62, 0.05);
    padding: 16px;
    height: 100%;
  }

  .promo-card {
    min-height: 140px;
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    background: linear-gradient(135deg, #ffffff 0%, #f5f8ff 100%);
  }

  .promo-card h3, .product-card h4 {
    margin: 0 0 6px;
    color: var(--dodla-text);
  }

  .promo-card p, .product-card p, .muted {
    margin: 0;
    color: var(--muted);
    font-size: 13px;
    line-height: 1.5;
  }

  .promo-emoji {
    font-size: 48px;
    line-height: 1;
    opacity: 0.92;
  }

  .category-btn {
    text-align: center;
    background: white;
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 16px 10px;
    font-size: 13px;
    font-weight: 700;
    color: var(--dodla-text);
    box-shadow: 0 8px 20px rgba(18,31,62,0.04);
  }

  .product-card {
    position: relative;
    overflow: hidden;
  }

  .badge {
    display: inline-block;
    font-size: 11px;
    font-weight: 700;
    padding: 4px 9px;
    border-radius: 999px;
    margin-right: 6px;
    margin-bottom: 8px;
  }

  .badge.sale { background: #ffe8e8; color: #c81e1e; }
  .badge.best { background: #fff3d6; color: #9a6400; }

  .product-emoji {
    font-size: 56px;
    margin: 8px 0 12px;
    line-height: 1;
  }

  .price-row {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 10px 0 14px;
    flex-wrap: wrap;
  }

  .sale-price {
    font-size: 20px;
    font-weight: 800;
    color: var(--dodla-blue);
  }

  .original-price {
    color: #9aa3b5;
    text-decoration: line-through;
    font-size: 13px;
  }

  .small {
    font-size: 12px;
    color: var(--muted);
  }

  .cart-box {
    background: linear-gradient(180deg, #ffffff, #f8fbff);
    border: 1px solid var(--line);
    border-radius: 22px;
    padding: 16px;
    margin-bottom: 18px;
  }

  .cart-item {
    display: flex;
    justify-content: space-between;
    gap: 10px;
    align-items: center;
    border-bottom: 1px solid rgba(0,0,0,0.06);
    padding: 10px 0;
    font-size: 14px;
  }

  .cart-total {
    font-size: 18px;
    font-weight: 800;
    color: var(--dodla-blue);
    margin-top: 14px;
  }

  .footer {
    background: linear-gradient(135deg, var(--dodla-blue), #0e4cb8);
    color: white;
    border-radius: 24px;
    padding: 28px;
    margin-top: 28px;
  }

  .footer h4 { margin: 0 0 10px; color: #ffd56a; }
  .footer p, .footer a { color: rgba(255,255,255,0.86); font-size: 13px; line-height: 1.8; text-decoration: none; }

  .faq-item summary {
    cursor: pointer;
    font-weight: 700;
    color: var(--dodla-text);
  }

  .faq-item {
    background: white;
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 14px 16px;
    margin-bottom: 10px;
  }

  .hidden-mobile { display: block; }

  @media (max-width: 900px) {
    .hero-grid, .promo-grid, .info-grid, .testimonial-grid, .category-grid {
      grid-template-columns: 1fr;
    }
    .hero h1 { font-size: 34px; }
    .hidden-mobile { display: none; }
  }
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# SESSION STATE
# -----------------------------
if "city" not in st.session_state:
    st.session_state.city = None
if "cart" not in st.session_state:
    st.session_state.cart = {}
if "show_cart" not in st.session_state:
    st.session_state.show_cart = False

# -----------------------------
# DATA
# -----------------------------
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
        {"name": "Full Cream Milk", "emoji": "🥛", "desc": "Rich & creamy full cream milk, 6% fat. Fresh from farms every morning.", "price": 68, "original": 75, "bestseller": True, "sale": True},
        {"name": "Standardised Milk", "emoji": "🥛", "desc": "Standardised cow milk with 4.5% fat. Perfect for everyday use.", "price": 52, "original": None, "bestseller": False, "sale": False},
        {"name": "Toned Milk", "emoji": "🥛", "desc": "Light & healthy toned milk with 3% fat. Great for health-conscious families.", "price": 44, "original": None, "bestseller": False, "sale": False},
        {"name": "Double Toned Milk", "emoji": "🥛", "desc": "Low-fat double toned milk with 1.5% fat. Ideal for weight management.", "price": 40, "original": 46, "bestseller": False, "sale": True},
        {"name": "Skimmed Milk", "emoji": "🥛", "desc": "Fat-free skimmed milk. Perfect for fitness enthusiasts and diabetics.", "price": 38, "original": None, "bestseller": False, "sale": False},
    ],
    "UHT Long Life Milk": [
        {"name": "UHT Full Cream Milk", "emoji": "📦", "desc": "Ultra-high temperature processed. Stays fresh for weeks. No boiling needed.", "price": 75, "original": 85, "bestseller": True, "sale": True},
        {"name": "UHT Toned Milk", "emoji": "📦", "desc": "Long-life toned milk. Convenient shelf-stable pack for daily use.", "price": 32, "original": None, "bestseller": False, "sale": False},
        {"name": "UHT Double Toned Milk", "emoji": "📦", "desc": "Light & long-lasting. Great for travel and pantry storage.", "price": 30, "original": None, "bestseller": False, "sale": False},
    ],
    "Curd & Buttermilk": [
        {"name": "Fresh Curd – Toned", "emoji": "🫙", "desc": "Thick, creamy toned curd. Available in pouches, cups & buckets.", "price": 55, "original": 65, "bestseller": True, "sale": True},
        {"name": "Fresh Curd – Double Toned", "emoji": "🫙", "desc": "Light and probiotic-rich double toned curd. Great for digestion.", "price": 48, "original": None, "bestseller": False, "sale": False},
        {"name": "Spiced Buttermilk", "emoji": "🥤", "desc": "Refreshing buttermilk with a hint of spices. Perfect for summer.", "price": 20, "original": 25, "bestseller": False, "sale": True},
        {"name": "Plain Buttermilk", "emoji": "🥤", "desc": "Pure and natural buttermilk. Light on stomach, rich in probiotics.", "price": 18, "original": None, "bestseller": False, "sale": False},
    ],
    "Ghee": [
        {"name": "Pure Cow Ghee", "emoji": "🫙", "desc": "Traditional cow ghee with rich aroma and golden colour.", "price": 584, "original": 650, "bestseller": True, "sale": True},
        {"name": "Pure Buffalo Ghee", "emoji": "🫙", "desc": "Creamy buffalo milk ghee. Dense texture for sweets & cooking.", "price": 636, "original": None, "bestseller": False, "sale": False},
        {"name": "High Aroma Ghee", "emoji": "✨", "desc": "Special high-aroma ghee with intense fragrance. Elevate every meal.", "price": 699, "original": 799, "bestseller": False, "sale": True},
    ],
    "Paneer & Sweets": [
        {"name": "Fresh Paneer", "emoji": "🧀", "desc": "Soft, fresh malai paneer made from full-cream milk. 200g block.", "price": 90, "original": 110, "bestseller": True, "sale": True},
        {"name": "Masala Paneer", "emoji": "🧀", "desc": "Spice-marinated paneer. Ready to cook for quick meals.", "price": 110, "original": None, "bestseller": False, "sale": False},
        {"name": "Doodh Peda", "emoji": "🍬", "desc": "Traditional milk sweets made from pure Dodla milk.", "price": 120, "original": 140, "bestseller": False, "sale": True},
    ],
    "Flavoured Milk & Lassi": [
        {"name": "Chocolate Flavoured Milk", "emoji": "🍫", "desc": "Rich cocoa milk drink. Kids love it. Packed with calcium & energy.", "price": 45, "original": 55, "bestseller": True, "sale": True},
        {"name": "Badam Milk", "emoji": "🌰", "desc": "Almond-infused flavoured milk with a traditional taste.", "price": 50, "original": None, "bestseller": False, "sale": False},
        {"name": "Rose Lassi", "emoji": "🌹", "desc": "Creamy rose-flavoured lassi made with fresh curd.", "price": 35, "original": 40, "bestseller": False, "sale": True},
        {"name": "Mango Lassi", "emoji": "🥭", "desc": "Thick, refreshing mango lassi made with real pulp & fresh curd.", "price": 40, "original": None, "bestseller": False, "sale": False},
    ],
}

TESTIMONIALS = [
    {"name": "Priya S.", "text": "Fresh delivery every morning and the quality feels premium."},
    {"name": "Ravi K.", "text": "The app is easy to use and the subscription flow is smooth."},
    {"name": "Anjali M.", "text": "Great taste, neat packaging, and fast customer support."},
]

FAQS = [
    ("How do I place an order?", "Select your city, choose a product, and click Add to Cart. Then proceed to checkout."),
    ("Do you offer subscriptions?", "Yes, you can turn milk delivery into a recurring subscription in the sample request section."),
    ("Which cities are supported?", "Hyderabad, Bangalore, Chennai, Vijayawada, and Tirupati are enabled in this demo."),
]

CATEGORY_ORDER = list(PRODUCTS.keys())

# -----------------------------
# HELPERS
# -----------------------------
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


def render_section_title(title: str, subtitle: str = ""):
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)
    if subtitle:
        st.markdown(f'<div class="section-subtitle">{subtitle}</div>', unsafe_allow_html=True)


def all_products():
    items = []
    for category, plist in PRODUCTS.items():
        for p in plist:
            items.append((category, p))
    return items


# -----------------------------
# CITY PICKER (first run)
# -----------------------------
if st.session_state.city is None:
    st.markdown(
        """
        <div class="hero">
          <div class="hero-grid">
            <div>
              <div class="pill">🥛 Fresh dairy delivered daily</div>
              <h1>Welcome to <span>Dodla Dairy</span></h1>
              <p>
                Select your city to start browsing milk, curd, paneer, ghee, and flavoured dairy products.
                This layout is designed to feel like a premium dairy ecommerce site.
              </p>
              <div class="hero-actions">
                <div class="pill">🚚 Free delivery above ₹299</div>
                <div class="pill">⭐ Premium quality</div>
                <div class="pill">📦 Subscription-friendly</div>
              </div>
            </div>
            <div class="hero-card">
              <div class="hero-emoji">🐄</div>
              <h3 style="margin:0 0 8px;">Choose your city</h3>
              <p style="margin:0 0 14px; opacity:0.92;">We deliver fresh dairy products across South India.</p>
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

# -----------------------------
# TOP BAR / NAV
# -----------------------------
st.markdown(
    f'<div class="topbar">🚚 Free delivery on orders above ₹299 | Delivering in <strong>{st.session_state.city}</strong> | Established 1995</div>',
    unsafe_allow_html=True,
)

nav_left, nav_mid, nav_right = st.columns([1.1, 2.8, 1.1])
with nav_left:
    st.markdown('<div class="brand">Dodla <span>Dairy</span> 🥛</div>', unsafe_allow_html=True)

with nav_mid:
    search_query = st.text_input(
        "",
        placeholder="Search products, categories, or favorites…",
        label_visibility="collapsed",
    )

with nav_right:
    chosen = st.selectbox("City", [f"📍 {c}" for c in CITIES], index=CITIES.index(st.session_state.city), label_visibility="collapsed")
    new_city = chosen.replace("📍 ", "")
    if new_city != st.session_state.city:
        st.session_state.city = new_city
        st.rerun()

st.markdown(
    """
    <div class="navbar">
      <div class="nav-links" style="justify-content:flex-start; flex:1;">
        <a class="nav-link" href="#shop">Products</a>
        <a class="nav-link" href="#offers">Offers</a>
        <a class="nav-link" href="#stories">Stories</a>
        <a class="nav-link" href="#faq">FAQs</a>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

# -----------------------------
# HERO
# -----------------------------
st.markdown(
    f"""
    <div class="hero">
      <div class="hero-grid">
        <div>
          <div class="pill">🥛 Fresh milk. Pure taste. Daily delivery.</div>
          <h1>Milk, curd & daily essentials, <span>delivered fresh</span></h1>
          <p>
            Explore Dodla’s premium dairy range in a polished ecommerce layout inspired by top modern dairy websites.
            Choose your products, add them to cart, and checkout in a clean, premium flow.
          </p>
          <div class="hero-actions">
            <div class="pill">🚚 Free delivery above ₹299</div>
            <div class="pill">⏱️ Morning delivery slots</div>
            <div class="pill">⭐ Premium quality</div>
          </div>
        </div>
        <div class="hero-card">
          <div class="hero-emoji">🐄</div>
          <div style="font-size:18px;font-weight:800; margin-bottom:6px;">Fresh from farm to fridge</div>
          <div style="font-size:13px; opacity:0.92; line-height:1.6;">Serving {st.session_state.city} with curated dairy essentials, subscriptions, and family favorites.</div>
          <div class="hero-mini">
            <div class="mini-stat"><h3>24h</h3><p>delivery feel</p></div>
            <div class="mini-stat"><h3>5</h3><p>cities</p></div>
            <div class="mini-stat"><h3>100%</h3><p>freshness</p></div>
          </div>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# PROMO BANNERS
# -----------------------------
st.markdown('<div id="offers"></div>', unsafe_allow_html=True)
render_section_title("Special offers", "Highlight a few premium campaigns just like a modern dairy storefront.")
promo_cols = st.columns(3)
promos = [
    ("Morning milk plan", "Start a recurring delivery subscription.", "🕗"),
    ("Family pack savings", "Buy more and save on bulk dairy essentials.", "🎁"),
    ("Paneer for dinner", "Fresh paneer and masala paneer for quick meals.", "🧀"),
]
for c, (title, desc, emoji) in zip(promo_cols, promos):
    with c:
        st.markdown(
            f"""
            <div class="card promo-card">
              <div>
                <h3>{title}</h3>
                <p>{desc}</p>
              </div>
              <div class="promo-emoji">{emoji}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# -----------------------------
# CATEGORIES
# -----------------------------
st.markdown('<div id="shop"></div>', unsafe_allow_html=True)
render_section_title("Shop by category", "Premium category tiles for a cleaner ecommerce-style homepage.")
cat_cols = st.columns(5)
category_icons = {
    "Fresh Milk": "🥛",
    "UHT Long Life Milk": "📦",
    "Curd & Buttermilk": "🫙",
    "Ghee": "✨",
    "Paneer & Sweets": "🧀",
    "Flavoured Milk & Lassi": "🍫",
}
for idx, cat in enumerate(CATEGORY_ORDER):
    with cat_cols[idx % 5]:
        st.markdown(
            f"""
            <div class="category-btn">
              <div style="font-size:28px; margin-bottom:8px;">{category_icons.get(cat, '🥛')}</div>
              {cat}
            </div>
            """,
            unsafe_allow_html=True,
        )

# -----------------------------
# MAIN SHOP + CART
# -----------------------------
shop_col, cart_col = st.columns([2.2, 1])

with shop_col:
    if search_query:
        q = search_query.lower().strip()
        items = [(cat, p) for cat, p in all_products() if q in p["name"].lower() or q in cat.lower()]
        render_section_title("Search results", f"Matching products for “{search_query}”.")
    else:
        items = all_products()
        render_section_title("Best sellers & daily essentials", "A premium product grid with city-aware pricing and easy add-to-cart actions.")

    if not items:
        st.info("No products matched your search.")
    else:
        # 3-column responsive product cards
        for i in range(0, len(items), 3):
            row = items[i:i+3]
            cols = st.columns(3)
            for col, (category, product) in zip(cols, row):
                with col:
                    price = city_price(product["price"])
                    original = city_price(product["original"]) if product["original"] else None
                    st.markdown(
                        f"""
                        <div class="card product-card">
                          <div>
                            {'<span class="badge best">Best seller</span>' if product['bestseller'] else ''}
                            {'<span class="badge sale">Sale</span>' if product['sale'] else ''}
                            <div class="product-emoji">{product['emoji']}</div>
                            <h4>{product['name']}</h4>
                            <div class="small">{category}</div>
                            <p style="margin-top:8px;">{product['desc']}</p>
                          </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                    st.markdown('<div style="height:6px;"></div>', unsafe_allow_html=True)
                    st.markdown(
                        f"<div class='price-row'><div class='sale-price'>₹{price}</div>{f"<div class='original-price'>₹{original}</div>" if original else ''}</div>",
                        unsafe_allow_html=True,
                    )
                    if st.button(f"Add to cart — {product['name']}", key=f"add_{category}_{product['name']}", use_container_width=True):
                        add_to_cart(product["name"], price)
                        st.toast(f"Added {product['name']} to cart")
                        st.rerun()

with cart_col:
    st.markdown(
        f"""
        <div class="cart-box">
          <div style="display:flex; justify-content:space-between; align-items:center; gap:10px;">
            <div>
              <div style="font-size:18px; font-weight:800; color:var(--dodla-blue);">🛒 Cart</div>
              <div class="small">{cart_count()} item(s)</div>
            </div>
            <div style="font-size:28px;">🧺</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not st.session_state.cart:
        st.info("Your cart is empty. Add some products from the shop.")
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
            st.markdown("---")

        st.markdown(f"<div class='cart-total'>Total: ₹{cart_total()}</div>", unsafe_allow_html=True)
        st.caption("Checkout is demo-only in this file. Connect Razorpay or Stripe for live payments.")
        if st.button("Checkout", type="primary", use_container_width=True):
            st.success("Order placed! Connect a payment gateway and order backend next.")
            st.session_state.cart = {}
            st.rerun()

# -----------------------------
# WHY DODLA
# -----------------------------
st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
render_section_title("Why choose Dodla", "A polished trust section, similar to modern ecommerce dairy pages.")
info_cols = st.columns(4)
info_data = [
    ("🏭", "Farm fresh", "Milk sourced and packaged for freshness."),
    ("🚚", "Fast delivery", "Daily delivery experience across supported cities."),
    ("🧾", "Easy ordering", "Simple cart and checkout flow."),
    ("⭐", "Premium quality", "Consistent dairy essentials and family favorites."),
]
for c, (emoji, title, desc) in zip(info_cols, info_data):
    with c:
        st.markdown(
            f"""
            <div class="card">
              <div style="font-size:34px; margin-bottom:10px;">{emoji}</div>
              <h3 style="margin:0 0 8px;">{title}</h3>
              <p>{desc}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# -----------------------------
# TESTIMONIALS
# -----------------------------
st.markdown('<div id="stories"></div>', unsafe_allow_html=True)
render_section_title("What customers say", "A section like Provilac’s story/review blocks, adapted for Dodla.")
review_cols = st.columns(3)
for c, review in zip(review_cols, TESTIMONIALS):
    with c:
        st.markdown(
            f"""
            <div class="card">
              <div style="font-size:24px;">★★★★★</div>
              <p style="margin:10px 0 14px; color:var(--dodla-text); font-size:14px; line-height:1.7;">“{review['text']}”</p>
              <div style="font-weight:700; color:var(--dodla-blue);">{review['name']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# -----------------------------
# SAMPLE REQUEST / SUBSCRIPTION FORM
# -----------------------------
render_section_title("Request a sample / subscribe", "Capture leads like a premium dairy ecommerce site.")
left, right = st.columns([1.2, 1])
with left:
    with st.form("sample_form"):
        name = st.text_input("Full name")
        mobile = st.text_input("Mobile number")
        city = st.selectbox("City", CITIES, index=CITIES.index(st.session_state.city))
        product = st.selectbox("Product", [p["name"] for _, p in all_products()])
        note = st.text_area("Delivery notes", placeholder="Apartment name, landmark, delivery time, etc.")
        submitted = st.form_submit_button("Request sample / subscribe")
        if submitted:
            st.success(f"Thanks {name or 'there'} — your request for {product} in {city} is noted.")
with right:
    st.markdown(
        """
        <div class="card">
          <h3 style="margin:0 0 10px; color:var(--dodla-blue);">📱 Premium delivery experience</h3>
          <p style="margin:0; line-height:1.8;">
            This section works well as your lead capture, subscription request, or contact form.
            It matches the style of a modern D2C dairy homepage without needing a full backend.
          </p>
          <div style="margin-top:14px;" class="small">Suggested next step: connect this form to email, CRM, or a database.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------
# FAQ
# -----------------------------
st.markdown('<div id="faq"></div>', unsafe_allow_html=True)
render_section_title("Frequently asked questions", "Simple expandable answers for a clean ecommerce experience.")
for question, answer in FAQS:
    with st.expander(question):
        st.write(answer)

# -----------------------------
# FOOTER
# -----------------------------
footer_cols = st.columns(4)
with footer_cols[0]:
    st.markdown(
        """
        <div class="footer">
          <h4>Dodla Dairy</h4>
          <p>Fresh dairy products with a premium shopping experience.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with footer_cols[1]:
    st.markdown(
        """
        <div class="footer">
          <h4>Shop</h4>
          <p>Milk</p>
          <p>Curd</p>
          <p>Paneer</p>
          <p>Ghee</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with footer_cols[2]:
    st.markdown(
        """
        <div class="footer">
          <h4>Support</h4>
          <p>FAQs</p>
          <p>Delivery</p>
          <p>Orders</p>
          <p>Contact</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with footer_cols[3]:
    st.markdown(
        """
        <div class="footer">
          <h4>Contact</h4>
          <p>hello@dodla.com</p>
          <p>+91 00000 00000</p>
          <p>South India</p>
          <p>Privacy • Terms</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    f"""
    <div class="footer" style="margin-top:18px; text-align:center;">
      <div style="font-size:13px; opacity:0.9;">© 2026 Dodla Dairy • Delivering in {st.session_state.city}</div>
    </div>
    """,
    unsafe_allow_html=True,
)
