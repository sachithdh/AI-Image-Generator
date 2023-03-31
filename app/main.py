import os
import openai
from dotenv import load_dotenv

# Loading environment variables from a .env file
load_dotenv()

def generateImg(text, sz):
    openai.api_key = os.getenv("OPENAI_API_KEY")  # Setting the API key for OpenAI
    
    # Creating an image using given prompt text and image size
    img = openai.Image.create(
        prompt = text,
        n = 1,
        size = sz
    )

    return img["data"][0]["url"] # Returning the URL of the generated image
