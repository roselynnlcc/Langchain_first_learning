---
title: Langchain QA Chatbot
emoji: 💬
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: 1.30.0
app_file: app.py
pinned: false
---

# Q&A Chatbot

## Overview
This Q&A Chatbot is a Streamlit web application that uses the Langchain OpenAI library to provide responses to user queries. It's designed to be simple, user-friendly, and effective for quick information retrieval.

## Deployment
The Streamlit web application is deployed on Hugging Face Spaces. You can interact with the live application here: [Langchain QA Chatbot](https://huggingface.co/spaces/roselynnlcc/Langchain_QA_Chatbot).

## Features
- Streamlit-based web interface for easy interaction
- Integration with OpenAI's powerful GPT-3.5 language model
- Environment variable management for API keys

## Screenshot of Generated Text
![Screenshot of the Q&A Chatbot on HuggingFace](images/huggingFace_deployment_screenshot.png)

## Installation and Setup
1. Clone this repository.
2. Install the required dependencies:
`pip install -r requirements.txt`
3. Set up your `.env` file with your `OPEN_API_KEY` from OpenAI.
4. Run the app:
`streamlit run app.py`


## Usage
Enter your question in the input field and click "Ask the question" to receive a response from the model.

## Acknowledgments
- This project is inspired by Krish Naik's [Learn LangChain In 1 Hour With End To End LLM Project With Deployment In Huggingface Spaces](https://youtu.be/qMIM7dECAkc?si=UwM2Q7ahLFw_Ch8A). It showcases my learning and adaptations in applying Langchain's functionalities.
