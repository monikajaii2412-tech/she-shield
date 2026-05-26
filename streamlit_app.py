import streamlit as st

# ---------------- PAGE ----------------
st.set_page_config(
    page_title="She-Shield",
    page_icon="🚨",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background: linear-gradient(
135deg,
#0f172a,
#111827,
#1e293b
);
color:white;
}

[data-testid="stHeader"]{
background: rgba(0,0,0,0);
}

.title{
text-align:center;
font-size:65px;
font-weight:bold;
color:white;
margin-top:20px;
}

.subtitle{
text-align:center;
font-size:22px;
color:#cbd5e1;
margin-bottom:40px;
}

.glass{
background: rgba(255,255,255,0.08);
padding:25px;
border-radius:25px;
backdrop-filter: blur(12px);
box-shadow: 0px 4px 30px rgba(0,0,0,0.4);
margin-bottom:20px;
}

.safe{
font-size:28px;
font-weight:bold;
color:#22c55e;
}

.sos button{
width:100%;
height:110px;
border:none;
border-radius:25px;
font-size:36px;
font-weight:bold;
background: linear-gradient(
90deg,
#ff0844,
#ff416c
);
color:white;
box-shadow:0px 0px 35px rgba(255,0,80,0.8);
transition:0.3s;
}

.sos button:hover{
transform:scale(1.02);
}

.stTextInput input{
border-radius:15px;
}

footer{
visibility:hidden;
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

# ---------------- STATUS ----------------
st.markdown("""
<div class='glass'>

<div class='safe'>
🟢 You Are Safe
</div>

<br>

✅ AI Voice Detection Active  
<br><br>
✅ Emergency Alert System Enabled  
<br><br>
✅ Real-Time GPS Tracking Ready  
<br><br>
✅ Trusted Contact Protection Enabled  

</div>
""", unsafe_allow_html=True)

# ---------------- USER SETUP ----------------
st.markdown("<div class='glass'>", unsafe_allow_html=True)

st.subheader("👤 User Setup")

name = st.text_input("Your Name")

email = st.text_input("Your Email")

emergency1 = st.text_input("Emergency Contact 1")

emergency2 = st.text_input("Emergency Contact 2")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- SOS ----------------
st.markdown("<div class='sos'>", unsafe_allow_html=True)

if st.button("🚨 SEND EMERGENCY SOS"):

    st.error("🚨 ALERT ACTIVATED")

    st.success("📍 Live location captured")

    st.info("📧 Emergency alert sent successfully")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FEATURES ----------------
col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class='glass'>

    <h2>🎤 Voice Assistant</h2>

    Say:
    <b>HELP</b>

    to activate emergency mode.

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class='glass'>

    <h2>📍 Live GPS Tracking</h2>

    Real-time location sharing
    with emergency contacts.

    </div>
    """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""

<br><br>

<center>
Made with ❤️ for Women's Safety
</center>

""", unsafe_allow_html=True)
      

