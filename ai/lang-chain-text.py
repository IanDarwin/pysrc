import os
import sys
from pathlib import Path

from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# This assumes you have installed pre-reqs:
#   pip install langchain langchain-community openai

# Find OpenAI API key
file_path = Path.home() / '.openai-apikey.txt'
if not file_path.exists():
    print(f"You can't run this example until you create {file_path} with your OpenAI API key")
    sys.exit(1)
mykey = open(file_path).readline().rstrip()

os.environ["OPENAI_API_KEY"] = mykey;
llm = ChatOpenAI()

model = ChatOpenAI(model="gpt-4")

text_prompt=("Explain scene 1 of The Godfather"
             "in 100 words or less.")

messages = [
    SystemMessage(content="You are a skilled movie critic"),
    HumanMessage(content=text_prompt),
]

print("Sending request")
resp = model.invoke(messages)

print(resp)
