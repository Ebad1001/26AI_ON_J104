import os
from dotenv import load_dotenv
import google.generativeai as genai

# get your API key at: "https://aistudio.google.com/app/apikey"
load_dotenv(override=True) 
API_KEY = os.getenv("API_KEY")
# print(API_KEY)

# configure genai
genai.configure(api_key=API_KEY)

# set up the model
model = genai.GenerativeModel(model_name="gemini-2.5-flash")

# start a conversation
chat = model.start_chat(history=[])

print("Welcome to the Gemini Chatbot!\n")
file = open("chat.txt", "w")

try:
    user_input = input("You: ").lower()
    response = chat.send_message(user_input)
    file.write(f"User:    {user_input}\n\n")
    file.write(f"Chatbot: {response.text}\n\n")
    file.write("----------------------------")
    print("Response saved in file")
    
except Exception as e:
    print(f"An error occurred: {e}")

file.close()