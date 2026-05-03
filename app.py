import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()

# Setup Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# UI
st.set_page_config(page_title="AI Content Generator")
st.title("🚀 AI Content Generator (Groq)")

topic = st.text_input("Enter Topic")
tone = st.selectbox("Select Tone", ["Formal", "Casual", "Creative"])
format_type = st.selectbox("Select Format", ["Blog", "LinkedIn Post", "Tweet"])

if st.button("Generate Content"):
    if topic == "":
        st.warning("Please enter a topic")
    else:
        prompt = f"Write a {tone} {format_type} about {topic}"

        try:
            response = client.chat.completions.create(
                messages=[
                {"role": "system", "content": "You are a professional content writer."},
                {"role": "user", "content": prompt}
                ],
            model="llama-3.1-8b-instant"
)

            output = response.choices[0].message.content

            st.success("Content Generated Successfully!")
            st.write(output)

        except Exception as e:
            st.error(f"Error: {e}")