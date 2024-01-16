# Q&A Chatbot
from langchain_openai import OpenAI

from dotenv import load_dotenv
# To take environment variables from .env
load_dotenv()

import streamlit as st
import os

## Function to load OpenAI model and get responses
def get_openai_response(question):
    llm=OpenAI(openai_api_key=os.getenv('OPEN_API_KEY'), model='gpt-3.5-turbo-instruct', temperature=0.5)
    response=llm(question)
    return response

## Initialize our streamlit app
st.set_page_config(page_title="Q&A ChatBot Demo")

st.header("Langchain Application")

input=st.text_input("Input: ", key="input")

response = get_openai_response(input)

submit=st.button("Ask the question")

if submit:
    st.subheader("The response is ")
    st.write(response)