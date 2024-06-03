import streamlit as st
import streamlit.components.v1 as components

# Title of the chatbot
st.title(f":speech_balloon: Mental Health Chatbot")

# Custom styles for the chatbot
st.markdown("""
<style>
    .chat-container {
        z-index: 999;
        position: fixed;
        font-color: #000;
        font-family: Google Sans;
        chat-background: #f3f6fc;
        message-user-background: #d3e3fd;
        message-bot-background: #fff;
        bottom: 5px;
        right: 200px;
        top: 600px;
        width: 1200px;
        
    }
</style>
""", unsafe_allow_html=True)

# Embedding the Dialogflow chatbot using HTML
chatbot_html = f"""
<link rel="stylesheet" href="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/themes/df-messenger-default.css">
<script src="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/df-messenger.js"></script>

<df-messenger
  project-id="healthwithgemini"
  agent-id="56db423c-ad93-498f-973e-72239f62b319"
  language-code="en"
  max-query-length="-1">
  <df-messenger-chat
   chat-title="">
  </df-messenger-chat>
</df-messenger>
"""

# Using Streamlit's components.html to render the chatbot
components.html(chatbot_html, height=700,width=900, scrolling=True)
