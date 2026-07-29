
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv

load_dotenv()


templats = PromptTemplate(
    template="""this is helpful ai that good for you bhai make one days plave for this topics {topics}""" , 
    input_variables=["topics"]
)

prompt = templats.format(topics = "using the oats")
from langchain_groq import ChatGroq
import os 

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
)


chain = templats | llm

result = chain.invoke({
    "topics" : "using the paneer"
}) 

response = result.content

print(response)

