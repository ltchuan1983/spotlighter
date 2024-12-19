import os
from openai import AzureOpenAI
from dotenv import load_dotenv


load_dotenv(dotenv_path='.env')


endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
openai_api_key = os.environ["AZURE_OPENAI_API_KEY"]

client = AzureOpenAI(
    api_key=openai_api_key,
    azure_endpoint=endpoint,
    api_version='2024-08-01-preview'
)

user_content = [
    {
        "type": "text",
        "text": "Extract the following single car option (yes/no) for lexus 350h executive. --> 1. Parking Assistance (The car executes the parking itself. Differentiate from parking distance sensors)  2. Parking distance sensors, surround view camera"
    }
]


user_content.append({
        "type": "image_url",
        "image_url": {
            "url": "https://deploytest2024.blob.core.windows.net/vw-initial-deploy/image/lexus_nx/page_32_1.png",
            "detail": "low"
        }
    })

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "You are a car analyst"
        },
        {
            "role": "user",
            "content": user_content
        },
    ],
)

content = response.choices[0].message.content

print(content)
