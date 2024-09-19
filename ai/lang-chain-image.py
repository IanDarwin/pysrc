import openai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI

# This assumes you have installed pre-reqs:
#   pip install langchain openai

# Initialize OpenAI API key
openai.api_key = 'your-openai-api-key'

# Define a prompt template for generating an image description
prompt_template = PromptTemplate(
    input_variables=["description"],
    template="Generate an image of {description}."
)

# Set up the LLM chain with OpenAI as the language model
llm_chain = LLMChain(
    llm=OpenAI(),
    prompt=prompt_template
)

# Input prompt text
input_description = "Charles Darwin in modern-day Toronto"

# Generate prompt for image creation
generated_prompt = llm_chain.run({"description": input_description})

# Send the prompt to DALL·E to get an image (or use any image model API)
def generate_image(prompt_text):
    response = openai.Image.create(
        prompt=prompt_text,
        n=1,  # Generate one image
        size="1024x1024"
    )
    return response['data'][0]['url']

# Generate the image
image_url = generate_image(generated_prompt)

# Output the image URL
print(f"Generated Image URL: {image_url}")

