## Integrated our code with OpenAI API
from env_constants import openai_key
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.globals import set_verbose
from langchain.chains import SequentialChain
from langchain.memory import ConversationBufferMemory
import streamlit as st


## streamlit framework
st.title("Celebrity Search")
input_text=st.text_input("Enter a question about a celebrity: ")

## Prompt Template
first_input_prompt=PromptTemplate(
    input_variables=['name'],
    template='Tell me about the celebrity {name}.'
)

## Initialize Memory Objects
person_memory = ConversationBufferMemory(input_key='name', memory_key='person')
dob_memory = ConversationBufferMemory(input_key='person', memory_key='dob')
description_memory = ConversationBufferMemory(input_key='dob', memory_key='description')

## OpenAI LLMS initialisation
llm = OpenAI(openai_api_key=openai_key, temperature=0.8)
set_verbose(True)
chain1=LLMChain(llm=llm, prompt=first_input_prompt, output_key='person', memory=person_memory)



## Prompt Template
second_input_prompt=PromptTemplate(
    input_variables=['person'],
    template='When was {person} born?'
)

chain2=LLMChain(llm=llm, prompt=second_input_prompt, output_key='dob', memory=dob_memory)

## Prompt Template
third_input_prompt=PromptTemplate(
    input_variables=['dob'],
    template='Mention 5 major events happens around {dob} in the world.'
)

chain3=LLMChain(llm=llm, prompt=third_input_prompt, output_key='description', memory=description_memory)


parent_chain=SequentialChain(chains=[chain1, chain2, chain3], 
                             input_variables=['name'],
                             output_variables=['person', 'dob', 'description'])

if input_text:
    st.write(parent_chain.invoke({'name':input_text}))

    ## Display the memory
    with st.expander('Person Profile: '):
        st.info(person_memory.buffer)
    
    with st.expander('Major Events around the DOB in the world:'):
        st.info(description_memory.buffer)


