import requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Configuration
APPLICATION_URL = "https://your-application-url.com"
SLACK_API_TOKEN = "your-slack-api-token"
SLACK_CHANNEL = "#your-slack-channel"

def send_slack_message(message):
    client = WebClient(token=SLACK_API_TOKEN)
    try:
        response = client.chat_postMessage(channel=SLACK_CHANNEL, text=message)
        return response["ts"]
    except SlackApiError as e:
        print(f"Error sending Slack message: {e.response['error']}")

def check_application_status():
    try:
        response = requests.get(APPLICATION_URL)
        return response.status_code
    except requests.RequestException as e:
        print(f"Error making HTTP request: {e}")
        return None

def main():
    status_code = check_application_status()

    if status_code is not None and status_code != 200:
        message = f"ALERT: Application is responding with status code {status_code}!"
        timestamp = send_slack_message(message)
        print(f"Slack message sent with timestamp: {timestamp}")
    else:
        print("Application is healthy.")

if __name__ == "__main__":
    main()
