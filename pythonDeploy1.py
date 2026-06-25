import streamlit as st
from google import genai
st.markdown(
  """
  <h1 style='text-align: center;'> Your AI Assistant</h1>
  <p style='text-align: center; font-size:18px;'>
    How can I help you. Ask anything you like.
  </p>
  """,
  unsafe_allow_html=True,
)
#robo = genai.Client(api_key="MY_APIKEY")
robo = genai.Client(api_key=st.secrets["MY_APIKEY"])
mychat = robo.chats.create(model="gemini-flash-lite-latest")
#mychat = robo.chats.create(model="gemini-3.1-flash-lite")
#mychat = robo.chats.create(model="gemini-2.5-flash")
#Placeholder for the response
response_placeholder = st.empty()

question = st.text_input("", placeholder="Enter your question here and Press Send")

col1, col2, col3 = st.columns([4, 1, 4])

with col2:
  send =st.button("Send")

if send:
  response = mychat.send_message(question)
  response_placeholder.write(response.text)
