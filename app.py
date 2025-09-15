

import streamlit as st
import random
import streamlit.components.v1 as components

st.set_page_config(page_title="Random Review Picker", page_icon="⭐", layout="centered")

BUSINESS_NAME = "VIP Digital Hub - Web Design Company Bhopal"

# ================== CSS ==================
st.markdown("""
<style>
h1 {
    text-align: center;
    color: #0b5fff;
    font-size: 20px;
    margin-bottom: 5px;
}
h3 {
    text-align: center;
    color: #333333;
    font-weight: 300;
    margin-top: 0;
}

/* Review box */
.review-box {
    background-color: var(--primary-background-color);
    color: var(--text-color);
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    margin-top: 20px;
    font-size: 16px;
    line-height: 1.5;
    text-align: left;
}

/* Center container */
.center-div {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-top: 20px;
}

/* Buttons (same style for both) */
.custom-btn {
    padding: 14px 20px;
    border-radius: 12px;
    border: none;
    background: linear-gradient(90deg, #0b5fff, #0846b7);
    color: white;
    font-weight: 600;
    font-size: 16px;
    cursor: pointer;
    width: 250px;
    text-align: center;
    transition: 0.3s;
    margin-top: 10px;
}
.custom-btn:hover {
    background: linear-gradient(90deg, #0846b7, #0b5fff);
}

/* Copied message */
#msg {
    display: block;
    margin-top: 10px;
    font-weight: 600;
    font-size: 16px;
    color: green;
    text-align: left ;
}

/* Mobile adjustments */
@media (max-width: 768px) {
    .review-box { font-size: 18px; }
    .custom-btn { font-size: 18px; width: 80%; padding: 16px; }
}
</style>
""", unsafe_allow_html=True)

# ================== Title ==================
st.markdown(f"# ⭐ Welcome to {BUSINESS_NAME} Review Page")

# ================== Google Review URL ==================
GOOGLE_REVIEW_URL = "https://g.page/r/CVLwfId3SaCDEAE/review"

# ================== Load Reviews ==================
try:
    with open("reviews.txt", "r", encoding="utf-8") as f:
        reviews = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    reviews = []
    st.error("⚠️ reviews.txt file not found!")

# ================== Main ==================
if reviews:
    # Center the Generate Random Review button
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("🎲 Generate Random Review"):
            selected_review = random.choice(reviews)
            st.markdown(f"<div class='review-box'>✍️ {selected_review}</div>", unsafe_allow_html=True)

            safe_review_js = repr(selected_review)
            html = f"""
            <div class="center-div">
                <button class="custom-btn" id="copyBtn">📋 Copy & Go Review Page </button>
                <span id="msg"></span>
            </div>
            <script>
            const reviewText = {safe_review_js};
            const copyBtn = document.getElementById('copyBtn');
            const msg = document.getElementById('msg');
            copyBtn.onclick = async () => {{
                try {{
                    await navigator.clipboard.writeText(reviewText);
                    msg.innerText = "Copied ✔ Redirecting to Google Reviews...";
                    window.open('{GOOGLE_REVIEW_URL}', '_blank');
                }} catch (err) {{
                    msg.innerText = "Copy failed — please copy manually.";
                }}
            }};
            </script>
            """
            components.html(html, height=200)
else:
    st.warning("No reviews found in reviews.txt! Please add some reviews.")


