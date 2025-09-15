
import streamlit as st
import random
import streamlit.components.v1 as components

st.set_page_config(page_title="Artistic_nails_by_Rajan Review Picker", page_icon="⭐", layout="centered")

# ===== Title + Styles =====
st.markdown("""
    <style>
        .title-text {
            text-align: center;
            font-size: 36px;
        }
        @media (max-width: 768px) {
            .title-text {
                font-size: 24px !important;
            }
        }

        .review-box {
            background-color: #f1f3f6;
            color: #000000;
            border-radius: 10px;
            padding: 15px;
            font-size: 18px;
            margin-top: 20px;
        }

        /* 🌙 Dark mode support */
        @media (prefers-color-scheme: dark) {
            .review-box {
                background-color: #1e1e1e !important;
                color: #ffffff !important;
            }
        }

        .custom-btn {
            background-color: #0b5fff;
            color: white;
            padding: 18px 30px;
            font-size: 20px;
            font-weight: 600; 
            border: none;
            border-radius: 10px;
            cursor: pointer;
            margin-top: 20px;
            width: 280px; 
        }

        .custom-btn:hover {
            background-color: #0846b7;
        }
    </style>

    <h1 class="title-text">⭐ Welcome to Artistic_nails_by_Rajan Review Page</h1>
""", unsafe_allow_html=True)

# ===== Google Review URL =====
GOOGLE_REVIEW_URL = "https://g.page/r/Cff9b0HSzthNEAE/review"

# ===== Load Reviews =====
try:
    with open("reviews.txt", "r", encoding="utf-8") as f:
        reviews = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    reviews = []
    st.error("⚠️ reviews.txt file not found!")

# ===== Session state to store selected review =====
if "selected_review" not in st.session_state:
    st.session_state.selected_review = ""

# ===== Generate Button =====
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🎲 Generate Random Review"):
        st.session_state.selected_review = random.choice(reviews)

# ===== Show Review and Copy/Go Button =====
if st.session_state.selected_review:
    review = st.session_state.selected_review
    st.markdown(f"<div class='review-box'>✍️ {review}</div>", unsafe_allow_html=True)

    # HTML + JS for Copy and Redirect
    safe_review = review.replace("'", "\\'")
    components.html(f"""
        <div style="text-align:center;">
            <button class="custom-btn" onclick="copyAndRedirect()"> Go to Google Review </button>
        </div>
        <script>
            function copyAndRedirect() {{
                const text = '{safe_review}';
                navigator.clipboard.writeText(text).then(() => {{
                    window.open('{GOOGLE_REVIEW_URL}', '_blank');
                }}).catch(err => {{
                    alert('Copy failed. Redirecting anyway.');
                    window.open('{GOOGLE_REVIEW_URL}', '_blank');
                }});
            }}
        </script>
    """, height=100)
else:
    st.info("👆 First generate a review to continue.")



