import streamlit as st
import openai
import speech_recognition as sr

st.set_page_config(page_title="PX Copilot", layout="centered")
st.title("🧠 PX Copilot")
st.subheader("Your Smart Interview Assistant")

openai.api_key = st.secrets["OPENAI_API_KEY"]

def transcribe_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Listening... Please speak clearly.")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand the audio."
        except sr.RequestError as e:
            return f"Could not request results; {e}"

# Text input or mic input
option = st.radio("Choose input method:", ["📝 Type your question", "🎤 Speak your question"])

if option == "📝 Type your question":
    prompt = st.text_area("✍️ What did the interviewer ask you?", "")
elif option == "🎤 Speak your question":
    if st.button("🎙️ Start Mic"):
        prompt = transcribe_audio()
        st.text_area("🎧 Transcribed Text", value=prompt, height=100)

# GPT response
if st.button("🤖 Generate Answer"):
    if prompt.strip() == "":
        st.warning("Please enter or speak a question first.")
    else:
        with st.spinner("Thinking..."):
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful and confident interview copilot."},
                    {"role": "user", "content": prompt}
                ]
            )
            st.success(response.choices[0].message.content)
