from fastapi import FastAPI
from fastapi import APIRouter
from typing import TypedDict
import os 

from dotenv import load_dotenv

load_dotenv()

def funcadd():
    return "thisis add function okay bhai "

def subtrfunc():
    return "this is subtarct function is available here"
 

class states(TypedDict):
    add : str 
    sub : str 


def funcoverall(state : states):
    state["add"] = funcadd()
    state["sub"] = subtrfunc()
    return state

state : states = {
    "add" : " "   , 
    "sub" : ""
}
result  = funcoverall(state)
# print(result)

# ------------- Getting the getmothods data -------------#
dic = {
    "name" : "ashish" , 
    "role" : "data engineer "
}


from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
)

result  = llm.invoke("what is full form of atm")
print(result.content)

from langgraph.graph import StateGraph


def function():
    return "this is function okay"



