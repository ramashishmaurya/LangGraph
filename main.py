import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

from langsmith import traceable

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
)


@traceable(name="langsmith-demo")
def chat(question: str):
    return llm.invoke(question)

response = chat("What is Artificial Intelligence?") 

@traceable
def summarize():
    response = chat("where we can use the ai ")

    finalresult = llm.invoke(f"summarize the this response in 10 line there is response {response}")

    return finalresult


finals = summarize()
print(finals.content)

