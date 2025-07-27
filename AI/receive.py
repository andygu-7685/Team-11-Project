# TODO: import your module
from openai import OpenAI
import base64
import requests
import os, time
import sys
from dotenv import load_dotenv

# load_dotenv()
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# # Get the folder where the script is located, done for you
# script_dir = os.path.dirname(os.path.abspath(__file__))
# filename = os.path.join(script_dir, "../frontend/public/downloaded_image.jpg") 
     
# You will have to change the IP Address


##TEST
load_dotenv()

ESP_IP   = os.getenv("ESP_IP", "192.168.4.74")
ESP_PORT = os.getenv("ESP_PORT", "80")
WIDTH    = os.getenv("ESP_WIDTH", "640")
HEIGHT   = os.getenv("ESP_HEIGHT", "480")
FORMAT   = os.getenv("ESP_FORMAT", "jpg")
TARGET   = os.getenv("DOWNLOAD_TARGET", "../frontend/public/downloaded_image.jpg")

##DEBUG and TIMEOUT parameters provided
def download_image(retries=3, timeout=5):
    # Build URL and target path
    url = f"http://{ESP_IP}:{ESP_PORT}/{WIDTH}x{HEIGHT}.{FORMAT}"
    print(f"DEBUG → Attempting download from: {url!r}")
    print(f"DEBUG → Will save to: {TARGET!r}")
    
    for attempt in range(1, retries + 1):
        try:
            print(f"[{attempt}] → GET {url}")
            r = requests.get(url, timeout=timeout)
            print(f"[{attempt}] ← Received status {r.status_code}")
            r.raise_for_status()
            
            # Ensure target directory exists
            dirpath = os.path.dirname(TARGET)
            print(f"[{attempt}] → Ensuring directory exists: {dirpath!r}")
            os.makedirs(dirpath, exist_ok=True)
            
            # Write the file
            print(f"[{attempt}] → Writing file...")
            with open(TARGET, "wb") as f:
                f.write(r.content)
            print(f"[{attempt}] ✅ Successfully saved image to {TARGET}")
            return

        except Exception as e:
            # Catch *any* exception so you see everything that goes wrong
            print(f"[{attempt}] ⚠️ attempt failed with error: {e!r}")

    print("DEBUG → All download attempts exhausted.")
    raise RuntimeError("All download attempts failed")



# TODO: Download the image and get a response from openai

if __name__ == "__main__":
    download_image()


def capture_image():
    return download_image()

# def encode_image_to_base64(image_path):
#     with open(image_path, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode("utf-8")

# image_path = filename
# base64_image = encode_image_to_base64(image_path)

# response = client.chat.completions.create(
#     model="gpt-4o",
#     messages=[
#         {
#             "role": "user",
#             "content": [
#                 {"type": "text", "text": "What's in this image?"},
#                 {
#                     "type": "image_url",
#                     "image_url": {
#                         "url": f"data:image/jpeg;base64,{base64_image}",
#                     },
#                 },
#             ],
#         }
#     ],
# )

# print(response.choices[0].message.content)

# # TODO: How to control when to take photo?

#On click of button from frontend, call call download_image() function to display the image in the frontend


