import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

## Function To get response from the LLama 2 model
def getLLamaResponse(input_text,no_words,blog_style):

    ### Llama 2 Model
    llm = CTransformers(model="models/llama-2-7b-chat.ggmlv3.q2_K.bin",
                        model_type='llama',
                        config={'max_new_tokens':256,
                                'temperature':0.01})
    
    ## Prompt Template
    template="""
        Write a blog for a typical {blog_style} on a topic {input_text}
        within {no_words} words.
            """
    prompt=PromptTemplate(input_variables=["blog_style","input_text","no_words"],
                          template=template)
    
    ## Generate the response from the Llama 2 model
    response=llm.invoke(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response

st.set_page_config(page_title="Blog Generation", 
                   page_icon="📝", 
                   layout="centered",
                   initial_sidebar_state='collapsed')

st.header("Blog Generation 📝")

input_text=st.text_input("Enter the blog topic: ")

## creating two more columns for addition 2 fields

col1, col2=st.columns([5,5])

with col1:
    no_words=st.text_input('No of words: ')
with col2:
    blog_style=st.selectbox('Writing the blog for: ', 
                            ('Fifth grader', 'University Student', 'Working Class', 'Retired Person'), index=0)
submit = st.button("Generate")

## Final response
if submit:
    st.write(getLLamaResponse(input_text,no_words,blog_style))
