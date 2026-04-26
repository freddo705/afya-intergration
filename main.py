import requests
import credentials as creds

# Step 1
print("Step 1: Starting handshake...")

response1 = requests.post(
    creds.BASE_URL + "/initiate-handshake",
    json={
        "platform_name": creds.PLATFORM_NAME,
        "platform_key": creds.PLATFORM_KEY,
        "platform_secret": creds.PLATFORM_SECRET,
        "callback_url": creds.CALLBACK_URL
    }
)

token = response1.json()["data"]["handshake_token"]
print("Token received:", token)

# Step 2
print("\nStep 2: Completing handshake...")

response2 = requests.post(
    creds.BASE_URL + "/complete-handshake",
    json={
        "handshake_token": token,
        "platform_key": creds.PLATFORM_KEY
    }
)

result = response2.json()
print("Access Token:", result["data"]["access_token"])
print("\nConnected to Afya Platform successfully")