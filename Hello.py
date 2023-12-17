import google.generativeai as genai
import streamlit as st
import apikey

api_key = apikey.key
genai.configure(api_key)

# Set up the model
generation_config = {
  "temperature": 0.6,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  }
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
quest=""
chat = model.start_chat(history=[])

st.title("Hello To My Gemini Experience")


quest = st.text_input("Enter your NEET question: ")
prompt_parts = [
  f"""You are the best all in one tutor in the world
You know each and every topic in this world
You are known for your explanation through funny real world examples
I am your student and I am learning as much as i could
Please answer every question of mine with a funny real world exampleand include code and output if needed
I will provide you a question and you should explain me the concept used in the question using examples
The question is {quest}"""
]

response = chat.send_message(prompt_parts)
st.write(response.text)




