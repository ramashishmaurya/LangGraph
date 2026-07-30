
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv

load_dotenv()
from langchain_core.output_parsers import StrOutputParser

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

parser  = StrOutputParser()


chain = templats | llm | parser

result = chain.invoke({
    "topics" : "using the paneer"
}) 


# with open("rs.txt" , "w") as file:
#     file.write(result) 

print(result)

# has to sense as folowe d

from typing import  TypedDict

