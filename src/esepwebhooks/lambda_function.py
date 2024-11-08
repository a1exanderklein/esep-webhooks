import os
import json
import requests

def function_handler(event):
    issueURL = event.get("issue", {}).get("html_url", "No URL")

    payload = json.dumps({"text": f"Issue Created: {issueURL}"})

    slack_url = os.getenv("SLACK_URL")
    headers = {'Content-Type': 'application/json'}
    response = requests.post(slack_url, headers=headers, data=payload)

    return response.text
