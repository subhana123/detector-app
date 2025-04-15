import streamlit as st
import pandas as pd

# Known Israeli barcode prefix
ISRAEL_EAN_PREFIX = "729"

# Example known Israeli companies
israeli_brands = [
    "Strauss", "Osem", "Teva", "Ahava", "SodaStream", "Netafim",
    "Check Point", "Elbit", "Tnuva", "Rami Levi"
]

st.set_page_config(page_title="🇮🇱 Israel Product Detector", layout="centered")
st.title("🕵️‍♂️ Israel Product Detector")

st.markdown("This app helps you check if a product may be from **Israel** based on barcode or brand.")

# --- Barcode Checker ---
st.subheader("📦 Barcode Prefix Check")
barcode = st.text_input("Enter product barcode (UPC/EAN):")

if barcode:
    if barcode.startswith(ISRAEL_EAN_PREFIX):
        st.success("✅ This product appears to be from **Israel** (EAN prefix 729).")
    else:
        st.info("❌ This barcode does **not** start with Israel's prefix (729).")

# --- Brand Checker ---
st.subheader("🏷️ Brand / Manufacturer Check")
brand = st.text_input("Enter brand or manufacturer name:")

if brand:
    brand_clean = brand.strip().lower()
    matches = [b for b in israeli_brands if brand_clean in b.lower()]

    if matches:
        st.success(f"✅ `{brand}` is a known Israeli brand.")
    else:
        st.warning(f"⚠️ `{brand}` not found in Israeli brand list. May not be from Israel.")

# --- Expandable Brand List ---
with st.expander("📋 View Known Israeli Brands"):
    st.write(pd.DataFrame(israeli_brands, columns=["Brand Name"]))
