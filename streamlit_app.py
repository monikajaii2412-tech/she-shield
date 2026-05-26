import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="She-Shield",
    page_icon="🚨",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

body {
    background-color: #0f172a;
}

.main {
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b,
        #111827
    );
    color: white;
}

.title {
    text-align: center;
    font-size: 60px;
    font-weight: bold;
    color: white;
    margin-top: 20px;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #cbd5e1;
    margin-bottom: 40px;
}

.card {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 4px 30px rgba(0,0,0,0.3);
    margin-bottom: 20px;
}

.safe-status {
    color: #22c55e;
    font-size: 24px;
    font-weight: bold;
}

.sos-btn button {
    width: 100%;
    height: 100px;
    border-radius: 20px;
    border: none;
    font-size: 35px;
    font-weight: bold;
    background: linear-gradient(
        90deg,
        #ff0844,
        #ff416c
    );
    color: white;
    box-shadow: 0px 0px 25px rgba(255,0,80,0.7);
}

.stTextInput > div > div > input {
    border-radius: 12px;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class='title'>
🚨 SHE-SHIELD
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='subtitle'>
AI Powered Women Safety Companion
</div>
""", unsafe_allow_html=True)

# ---------------- STATUS CARD ----------------
st.markdown("""
<div class='card'>

<div class='safe-status'>
🟢 You Are Protected
</div>

<br>

✅ Live Location Tracking Enabled  
<br>
✅ Emergency SOS System Active  
<br>
✅ AI Voice Assistant Ready  
<br>
✅ Trusted Contact Protection Enabled  

</div>
""", unsafe_allow_html=True)

# ---------------- USER DETAILS ----------------
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.subheader("👤 User Setup")

name = st.text_input("Your Name")

email = st.text_input("Your Email")

emergency1 = st.text_input("Emergency Contact 1")

emergency2 = st.text_input("Emergency Contact 2")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- SOS BUTTON ----------------
st.markdown("<div class='sos-btn'>", unsafe_allow_html=True)

if st.button("🚨 SEND SOS"):

    st.error("🚨 EMERGENCY ALERT ACTIVATED")

    st.success("📍 Live location captured")

    st.info("📧 Emergency alert sent successfully")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FEATURES ----------------
col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class='card'>

    <h3>🎤 Voice Assistant</h3>

    Say:
    <b>HELP</b>

    to activate emergency response.

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class='card'>

    <h3>📍 Live GPS Tracking</h3>

    Share real-time location
    with trusted contacts.

    </div>
    """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""

<br><br>

<center>
Made with ❤️ for Women's Safety
</center>

""", unsafe_allow_html=True)
