
# import streamlit as st
# import random
# import streamlit.components.v1 as components

# st.set_page_config(page_title="Artistic_nails_by_Rajan Review Picker", page_icon="⭐", layout="centered")

# # ===== Title + Styles =====
# st.markdown("""
#     <style>
#         .title-text {
#             text-align: center;
#             font-size: 36px;
#         }
#         @media (max-width: 768px) {
#             .title-text {
#                 font-size: 24px !important;
#             }
#         }

#         .review-box {
#             background-color: #f1f3f6;
#             color: #000000;
#             border-radius: 10px;
#             padding: 15px;
#             font-size: 18px;
#             margin-top: 20px;
#         }

#         /* 🌙 Dark mode support */
#         @media (prefers-color-scheme: dark) {
#             .review-box {
#                 background-color: #1e1e1e !important;
#                 color: #ffffff !important;
#             }
#         }

#         .custom-btn {
#             background-color: #0b5fff;
#             color: white;
#             padding: 18px 30px;
#             font-size: 20px;
#             font-weight: 600; 
#             border: none;
#             border-radius: 10px;
#             cursor: pointer;
#             margin-top: 20px;
#             width: 280px; 
#         }

#         .custom-btn:hover {
#             background-color: #0846b7;
#         }
#     </style>

#     <h1 class="title-text">⭐ Welcome to Artistic_nails_by_Rajan Review Page</h1>
# """, unsafe_allow_html=True)

# # ===== Google Review URL =====
# GOOGLE_REVIEW_URL = "https://g.page/r/Cff9b0HSzthNEAE/review"

# # ===== Load Reviews =====
# try:
#     with open("reviews.txt", "r", encoding="utf-8") as f:
#         reviews = [line.strip() for line in f if line.strip()]
# except FileNotFoundError:
#     reviews = []
#     st.error("⚠️ reviews.txt file not found!")

# # ===== Session state to store selected review =====
# if "selected_review" not in st.session_state:
#     st.session_state.selected_review = ""

# # ===== Generate Button =====
# col1, col2, col3 = st.columns([1, 2, 1])
# with col2:
#     if st.button("🎲 Generate Random Review"):
#         st.session_state.selected_review = random.choice(reviews)

# # ===== Show Review and Copy/Go Button =====
# if st.session_state.selected_review:
#     review = st.session_state.selected_review
#     st.markdown(f"<div class='review-box'>✍️ {review}</div>", unsafe_allow_html=True)

#     # HTML + JS for Copy and Redirect
#     safe_review = review.replace("'", "\\'")
#     components.html(f"""
#         <div style="text-align:center;">
#             <button class="custom-btn" onclick="copyAndRedirect()"> Go to Google Review </button>
#         </div>
#         <script>
#             function copyAndRedirect() {{
#                 const text = '{safe_review}';
#                 navigator.clipboard.writeText(text).then(() => {{
#                     window.open('{GOOGLE_REVIEW_URL}', '_blank');
#                 }}).catch(err => {{
#                     alert('Copy failed. Redirecting anyway.');
#                     window.open('{GOOGLE_REVIEW_URL}', '_blank');
#                 }});
#             }}
#         </script>
#     """, height=100)
# else:
#     st.info("👆 First generate a review to continue.")


import streamlit as st
import base64
from pathlib import Path
import re

st.set_page_config(page_title="Artistic_nails_by_Rajan ", layout="wide")

# --- 1️⃣ Load HTML content ---
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()



# --- 2️⃣ Embed images as base64 ---
def encode_file_to_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Background image
bg_base64 = encode_file_to_base64("background.jpg")
html_content = html_content.replace(
    "url('background.jpg')",
    f"url('data:image/jpeg;base64,{bg_base64}')"
)

# Logo
logo_base64 = encode_file_to_base64("logo.png")
html_content = html_content.replace(
    '<img src="logo.png"',
    f'<img src="data:image/png;base64,{logo_base64}"'
)

# --- 3️⃣ Embed reviews.txt into JS ---
with open("reviews.txt", "r", encoding="utf-8") as f:
    reviews = [line.strip() for line in f if line.strip() != ""]

reviews_js_array = str(reviews)

# Replace loadReview function
load_review_js = f"""
function loadReview() {{
    const reviews = {reviews_js_array};
    if(reviews.length === 0) {{
        reviewText.textContent = "No reviews available!";
        return;
    }}
    const randomIndex = Math.floor(Math.random() * reviews.length);
    review = reviews[randomIndex];
    reviewText.textContent = review;
}}
"""
html_content = re.sub(r'function loadReview\(\)\s*{{.*?}}', load_review_js, html_content, flags=re.DOTALL)

# --- 4️⃣ Embed CSS inline ---
css_files = ["./static/css/index.BOl9eq08.css"]  # Add more CSS files if needed
for css_file in css_files:
    path = Path(css_file)
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            css_content = f.read()
        # Remove crossorigin and embed
        link_tag_pattern = re.escape(f'<link rel="stylesheet" crossorigin href="{css_file}">')
        html_content = re.sub(link_tag_pattern, f"<style>{css_content}</style>", html_content)

# --- 5️⃣ Embed JS inline ---
js_files = ["./static/js/main.js"]  # Add more JS files if needed
for js_file in js_files:
    path = Path(js_file)
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            js_content = f.read()
        # Remove crossorigin and embed
        script_tag_pattern = re.escape(f'<script src="{js_file}" crossorigin></script>')
        html_content = re.sub(script_tag_pattern, f"<script>{js_content}</script>", html_content)

# --- 6️⃣ Display HTML in Streamlit ---
st.components.v1.html(html_content, height=1000, scrolling=True)


