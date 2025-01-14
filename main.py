from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

import os

os.environ['GOOGLE_API_KEY']="AIzaSyD7S74_J15JdeH8GYtjXTiUE4ynOz87XL8"

tweet_template = "Give me {number} tweets on {topic}"

tweet_prompt = PromptTemplate(template= tweet_template, imput_variables =['number', 'topic'])

gemini_model= ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")

tweet_chain = tweet_prompt | gemini_model

response = tweet_chain.invoke({"number" : 5, "topic" : " Wars in Middle East"})


import streamlit as st

st.header("Tweet generator")

st.subheader("Generate tweets using GenAI")

topic= st.text_input("topic")

number=st.number_input("number of tweets", min_value=1, max_value=10, value=1, step=1)

if st.button("generate"):
 tweets = tweet_chain.invoke({"number" : number, "topic" : topic})
 st.write(tweets.content)