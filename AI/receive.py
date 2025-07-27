# TODO: import your module
from openai import OpenAI
import base64
import requests
import os
import sys
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Get the folder where the script is located, done for you
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, "../frontend/public/downloaded_image.jpg") 

url = "http://192.168.50.236/1024x768.jpg"             # You will have to change the IP Address

# Function to download the image from esp32, given to you
def download_image():
    response = requests.get(url)

    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
    #     print(f"Image saved to: {filename}")
    # else:
    #     print("Failed to download image. Status code:", response.status_code)

# TODO: Download the image and get a response from openai

download_image()




def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

image_path = filename
base64_image = encode_image_to_base64(image_path)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                    },
                },
            ],
        }
    ],
)

print(response.choices[0].message.content)

# TODO: How to control when to take photo?



