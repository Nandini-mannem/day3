
import requests

# Replace this with your actual Vapi API key
API_KEY = "YOUR_VAPI_API_KEY"

# Replace with your Assistant ID from Vapi
ASSISTANT_ID = "YOUR_ASSISTANT_ID"

# Your mobile number (with +91 if in India)
PHONE_NUMBER = "+91XXXXXXXXXX"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "phoneNumber": PHONE_NUMBER,
    "assistantId": ASSISTANT_ID
}

response = requests.post("https://api.vapi.ai/call/phone", headers=headers, json=data)

if response.status_code == 200:
    print("✅ Call queued successfully!")
else:
    print("❌ Error:", response.text)