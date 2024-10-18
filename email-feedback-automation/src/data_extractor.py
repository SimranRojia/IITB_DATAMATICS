import requests
import json

def extract_data(content):
    with open('config/trucap_config.json') as f:
        config = json.load(f)

    response = requests.post(
        config["api_url"],
        json={"documentText": content},
        headers={"Authorization": f"Bearer {config['auth_token']}"}
    )
    return response.json()
