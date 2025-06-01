
import streamlit as st

# Title
st.title("🧠 EmpathAI Core - Personality Drift Demo")

# Intro
st.markdown("""
This demo shows how the same input can generate different responses depending on the AI's **personality drift** setting.

Type a prompt below, then select a personality mode to see how EmpathAI might respond.
""")

# Input
user_input = st.text_area("💬 Enter your message or situation prompt:", "")

# Personality selection
personality = st.selectbox(
    "🧬 Choose a personality mode:",
    ("Empathetic", "Pragmatic", "Neutral")
)

# Placeholder responses
def generate_response(text, mode):
    if mode == "Empathetic":
        return f"🌿 [Empathetic] I hear you. That sounds difficult. You're not alone in feeling this way. Let's explore what matters to you."
    elif mode == "Pragmatic":
        return f"⚙️ [Pragmatic] Based on your input, here's what we can do to address it efficiently. Let's break it into steps."
    elif mode == "Neutral":
        return f"🧊 [Neutral] Understood. Here's an analysis of the situation without assumptions."

# Output
if user_input.strip():
    response = generate_response(user_input, personality)
    st.markdown("### 🗣️ EmpathAI Response")
    st.write(response)
else:
    st.info("Enter a message above to begin.")

# Footer
st.markdown("""
---
Made with ❤️ by [EmpathAI Core](https://github.com/uvx8299/EmpathAI-Core)
""")
