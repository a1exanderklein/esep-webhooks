import os
import json
import requests

def function_handler(input):
    data = json.loads(input)

    payload = {
        "text": f"Issue Created: {data['issue']['html_url']}"
    }

    slack_url = os.getenv("SLACK_URL")
    headers = {'Content-Type': 'application/json'}
    response = requests.post(slack_url, headers=headers, data=json.dumps(payload))

    return response.text
