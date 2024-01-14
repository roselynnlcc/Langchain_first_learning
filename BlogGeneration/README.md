# BlogGeneration
The BlogGeneration project is a Streamlit application leveraging the *Langchain* library and the *Llama 2 model* for dynamic blog content creation. 

Users can input a topic, specify the number of words, and choose an audience style (e.g.  a Fifth Grader / University Student, Working-Class individual, or Retired Person). The application generates a tailored blog post.

## Set up of environment
Regarding the set up of environment, please refer to Krish Naik's video titled [End to End LLM Project Using LLAMA 2](https://www.youtube.com/watch?v=cMJWC-csdK4&list=PLZoTAELRMXVORE4VF7WQ_fAl0L1Gljtar&index=9)

## Installation of dependencies
`pip install -r requirements.txt

## Run the App
`streamlit run app.py`


## Model Used
The project utilizes the Llama 2 model, selected for its compact size and efficient performance. This efficiency is achieved through a process called *'quantization'*, which optimizes the model to require less computational power without significantly compromising its effectiveness. 

You can find the model here: [Llama 2 Model](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q2_K.bin)

## Screenshot of Generated Text

![Screenshot of LLM Output](images/screenshot.png)