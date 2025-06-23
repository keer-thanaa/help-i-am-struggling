import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Help, I Am Struggling", page_icon="💛", layout="centered")

# Custom cozy styling
st.markdown(
    """
    <style>
        /* Main wrapper */
        .main-container {
            background-color: #fff9f4;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            margin-top: -40px;  /* removes extra white space */
        }
        textarea, .stTextInput > div > div > input {
            background-color: #fff5ea;
            border-radius: 10px;
            padding: 10px;
            color: #333;
        }
        .stButton button {
            background-color: #ffc8dd;
            color: black;
            border-radius: 10px;
            padding: 0.6em 1.2em;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)



# Title & intro
st.title("💛 Help, I Am Struggling")
st.markdown("#### This space is for you. You are safe here.")
st.markdown("Take your time. No pressure. Just breathe and let go a little.")

# Virtual hug & award
if st.button("🤝 I Need a Hug"):
    st.markdown("### 🤗 A big, warm hug to you, dear soul.")
    st.success("🏅 You showed up today — and that’s everything.")
    st.markdown("*You are so deeply loved, even on days you can't feel it.*")

# Venting area
st.markdown("---")
st.markdown("### 📝 Let It Out")
vent = st.text_area("What’s on your mind? What’s been hurting? You can say it all here.", height=200)

if vent:
    st.markdown("✅ You did it. You shared your truth — and that’s powerful.")
    st.markdown("*We hear you. We hold your words with love.*")

# Breathing exercise
st.markdown("---")
with st.expander("🧘‍♀️ Breathe With Me"):
    st.markdown("""
    ### 🌬️ Guided Calm
    Let’s do this together:
    - Inhale for **4 seconds**
    - Hold for **4 seconds**
    - Exhale slowly for **6 seconds**
    - Repeat a few times

    *You’re doing so well. One breath at a time.*  
    """)

# Quotes
with st.expander("💬 Gentle Words for Tough Days"):
    st.markdown("""
    > _“No feeling is final.”_ – Rainer Maria Rilke  
    >
    > _“You are not a burden. You are a human being with a heavy heart.”_  
    >
    > _“The fact that you're trying means you're not failing.”_  
    """)

