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

@traceable (name="summarixation" )
def summarize():
    response = chat("where we can use the ai ")

    finalresult = llm.invoke(f"summarize the this response in 10 line there is response {response}")

    return finalresult


@traceable(name='compression')

def summarizertwoline():
    callsumarize = summarize()

    prompts =f"this is my answer of 10 line on how i can explain to dump guys {callsumarize}"

    result = llm.invoke(prompts)

    return result

results = summarizertwoline()

print(results.content)

