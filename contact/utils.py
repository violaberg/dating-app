import requests
from django.conf import settings


def send_email(email, subject, message):
    api_key = settings.RESEND_API_KEY
    url = "https://api.resend.com/emails"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "from": "Your Name <onboarding@resend.dev>",
        "to": [email],
        "subject": subject,
        "html": f"<p>{message}</p>"
    }

    response = requests.post(url, json=data, headers=headers)
    return response.json()
