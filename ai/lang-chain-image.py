import os
import sys
from pathlib import Path

from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper
from langchain_openai import ChatOpenAI

# This assumes you have installed pre-reqs:
#   pip install langchain langchain-community openai

# As of this writing, the documentation on
# https://python.langchain.com/docs/integrations
# is NOT up to date, still recommending deprecated
# APIs. So this will have to change when 1.0
# is released.

# Find OpenAI API key
file_path = Path.home() / '.openai-apikey.txt'
if not file_path.exists():
    print(f"You can't run this example until you create {file_path} with your actual key")
    sys.exit(1)
open(file_path).readline()
mykey = open(file_path).readline().rstrip()

os.environ["OPENAI_API_KEY"] = mykey;
llm = ChatOpenAI()

# Define a prompt template for generating an image description
prompt_template = PromptTemplate(
    input_variables=["description"],
    template="Generate an image based on {description}.",
)

# Set up the LLM chain with OpenAI as the language model
llm_chain = LLMChain(llm=llm, prompt=prompt_template)

# Input prompt text
description = "Charles Darwin in modern-day Toronto"


# Generate the image
image_url = DallEAPIWrapper().run(
    llm_chain.run(llm_chain.run(description)))

    #     size="1024x1024"

# Output the image URL
print(f"Generated Image URL: {image_url}")

# Try to open in browser
import webbrowser

webbrowser.open(image_url)
