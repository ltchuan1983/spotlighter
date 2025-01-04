import requests
import json


class TopicExtractor:
    def __init__(self, cfg):
        self.config = cfg

    def run(self, text):
        prompt = self.prepare_prompt(text)

        # Define the URL and the payload
        url = "http://localhost:11434/api/generate"
        payload = {
            "model": "llama3.2-vision:11b",
            "prompt": prompt,
        }

        # Convert the payload to a JSON string
        data = json.dumps(payload)

        # Make the POST request
        response = requests.post(
            url, data=data, headers={"Content-Type": "application/json"}
        )

        if response.status_code == 200:
            list_dict_words = []
            for each_word in response.text.split("\n"):
                try:
                    data = json.loads(each_word)
                except:
                    pass
                list_dict_words.append(data)

        output = "".join(
            [word["response"] for word in list_dict_words if type(word) == type({})]
        )
        return output

    def prepare_prompt(self, text):
        prompt = self.config.mistral_prompt_1.replace("<<text>>", text)
        return prompt
