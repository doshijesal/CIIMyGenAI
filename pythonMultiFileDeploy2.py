import streamlit as st
from google import genai
from google.genai import types
config = types.GenerateContentConfig(
    system_instruction = """You are an expert Sports Enthusiast, Follower, Analyst, Record Keeper, Writer, Commentator, and Sports Fan.
 Answer only questions related to Sports programming.
 For any non-Sports question, reply exactly:
 Please ask a Sports-related question.
 Do not answer questions outside the Python domain."""
  )
st.markdown(
  """
  <h1 style='text-align: center;'> Your Sports AI Assistant</h1>
  <p style='text-align: center; font-size:18px;'>
    Ask any Sports question.
  </p>
  """,
  unsafe_allow_html=True,
)
robo = genai.Client( api_key=st.secrets["MY_API_KEY"])
mychat = robo.chats.create(model="gemini-flash-lite-latest")

Placeholder for the response
response_placeholder = st.empty()

question = st.text_input("", placeholder="Enter your Sports question here...")

col1, col2, col3 = st.columns([4, 1, 4])

with col2:
  send =st.button("Go...")
if send:
  response = mychat.send_message(question)
  response_placeholder.write(response.text)

mychat = robo.chats.create(model="gemini-flash-lite-latest")
#Placeholder for the response
response_placeholder = st.empty()

question = st.text_input("", placeholder="Enter your Python question here...")

col1, col2, col3 = st.columns([4, 1, 4])

with col2:
  send =st.button("Go...")

if send:
  question = question + config.system_instruction
  response = mychat.send_message(question)
  response_placeholder.write(response.text)
