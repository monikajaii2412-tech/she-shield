import streamlit as st
import streamlit.components.v1 as components
import smtplib
from email.mime.text import MIMEText

# ---------------- PAGE ----------------
st.set_page_config(page_title="Women Safety Guard", page_icon="🚨")

st.title("🚨 Women Safety Guard")

# ---------------- EMAIL CONFIG ----------------
SENDER_EMAIL = "yourgmail@gmail.com"
APP_PASSWORD = "your_app_password"

# ---------------- EMAIL FUNCTION ----------------
def send_email(to_email, subject, body):

    msg = MIMEText(body)

    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(SENDER_EMAIL, APP_PASSWORD)

    server.sendmail(SENDER_EMAIL, to_email, msg.as_string())

    server.quit()

# ---------------- SESSION STORAGE ----------------
if "saved" not in st.session_state:
    st.session_state.saved = False

# ---------------- FIRST TIME SETUP ----------------
if not st.session_state.saved:

    st.subheader("🔐 Setup Your Account")

    name = st.text_input("Your Name")
    user_email = st.text_input("Your Email")

    emergency1 = st.text_input("Emergency Email 1")
    emergency2 = st.text_input("Emergency Email 2")

    if st.button("Save Details"):

        st.session_state.name = name
        st.session_state.user_email = user_email
        st.session_state.emergency1 = emergency1
        st.session_state.emergency2 = emergency2

        st.session_state.saved = True

        st.success("Details Saved Successfully!")

        st.rerun()

# ---------------- MAIN APP ----------------
else:

    st.success(f"Welcome {st.session_state.name}")

    st.subheader("📍 Live Location Access")

    st.info("Allow location permission when browser asks.")

    # ---------------- JAVASCRIPT ----------------
    location_html = """
    <div>
        <button id="sosButton" onclick="sendLocation()">🚨 SEND SOS</button>

        <p id="status"></p>
    </div>

    <script>

    async function sendLocation() {

        if (navigator.geolocation) {

            navigator.geolocation.getCurrentPosition(showPosition);

        } else {

            document.getElementById("status").innerHTML =
            "Geolocation not supported";

        }
    }

    function showPosition(position) {

        let lat = position.coords.latitude;
        let lon = position.coords.longitude;

        let mapLink =
        "https://www.google.com/maps?q=" + lat + "," + lon;

        document.getElementById("status").innerHTML =
        "🚨 SOS Triggered! Location Captured.";

        // send values to streamlit
        const streamlitMsg = {
            lat: lat,
            lon: lon,
            map: mapLink
        };

        window.parent.postMessage({
            type: "streamlit:setComponentValue",
            value: streamlitMsg
        }, "*");
    }

    // ---------------- VOICE ----------------
    function startVoice() {

        const SpeechRecognition =
        window.SpeechRecognition ||
        window.webkitSpeechRecognition;

        const recognition = new SpeechRecognition();

        recognition.lang = "en-US";

        recognition.start();

        recognition.onresult = function(event) {

            const text =
            event.results[0][0].transcript.toLowerCase();

            if(text.includes("help")) {

                document.getElementById("status").innerHTML =
                "🎤 HELP detected! Sending SOS...";

                sendLocation();
            }
        }
    }

    </script>

    <button onclick="startVoice()">
    🎤 Start Voice Assistant
    </button>
    """

    data = components.html(location_html, height=300)

    # ---------------- SEND EMAIL ----------------
    if data:

        map_link = data["map"]

        message = f"""
🚨 EMERGENCY ALERT 🚨

Name: {st.session_state.name}

User Email:
{st.session_state.user_email}

Message:
HELP! I need immediate assistance.

Live Location:
{map_link}
"""

        try:

            send_email(
                st.session_state.emergency1,
                "🚨 Emergency Alert",
                message
            )

            if st.session_state.emergency2:

                send_email(
                    st.session_state.emergency2,
                    "🚨 Emergency Alert",
                    message
                )

            st.error("🚨 ALERT SENT SUCCESSFULLY!")

            st.write("📍 Location:")
            st.write(map_link)

        except Exception as e:

            st.error(f"Email failed: {e}")
