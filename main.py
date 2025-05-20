print("Let us run code")
import os
from langchain_community.llms import Together
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("TOGETHER_API_KEY")


# Initialize the together AI model
llm = Together(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
    temperature=0.7,
    max_tokens=512,
)
# Define the prompt template

prompt_template_name = PromptTemplate(
    input_variables=["locality"],
    template="""
    
    You are an expert in branding restaurants. Based on  the "{locality}", suggest:
    1. A unique, culturally appropriate restaurant's name and 
    2. A themed food menu with 10 dishes inspired by that locality.
    Be creative and engaging.
    
    """,
)



# Combine into a langchain chain

chain = LLMChain(llm=llm, prompt=prompt_template_name)

# Run the chain
locality = 'Nyeri'
response = chain.run(locality = locality)
print(response)
