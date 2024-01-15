## Integrated our code with OpenAI API
from constants import openai_key
from langchain_openai import OpenAI
import streamlit as st



## streamlit framework
st.title("Ask a question in OpenAI's GPT")
input_text=st.text_input("Enter a question that you would like to ask: ")

## OpenAI LLMS initialisation
llm = OpenAI(openai_api_key=openai_key, temperature=0.8)

if input_text:
    st.write(llm.invoke(input_text))
