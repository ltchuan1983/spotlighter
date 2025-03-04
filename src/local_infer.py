import requests
import json

# Define the URL and the payload
url = "http://localhost:11434/api/generate"
payload = {
    "model": "mistral:instruct",
    "prompt": "Are car door mirrors with memorized positions usually electronic in nature?",
}

# Convert the payload to a JSON string
data = json.dumps(payload)


# Make the POST request
response = requests.post(url, data=data, headers={"Content-Type": "application/json"})
print(response)

if response.status_code == 200:
    list_dict_words = []
    for each_word in response.text.split("\n"):
        try:
            data = json.loads(each_word)
        except:
            pass
        list_dict_words.append(data)

llama_response = "".join(
    [word["response"] for word in list_dict_words if type(word) == type({})]
)
print(llama_response)
