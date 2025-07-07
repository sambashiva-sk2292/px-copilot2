import streamlit as st
import openai

st.set_page_config(page_title="PX Copilot", layout="centered")

st.title("🧠 PX Copilot")
st.subheader("Your Smart Interview Assistant")

openai.api_key = st.secrets["OPENAI_API_KEY"]

prompt = st.text_area("🎤 What did the interviewer ask you?", "")

if st.button("🧠 Generate Answer"):
    with st.spinner("Thinking..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful and confident interview copilot."},
                {"role": "user", "content": prompt}
            ]
        )
        st.success(response.choices[0].message.content)
