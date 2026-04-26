import requests
import credentials as creds

print("Step 1: Starting handshake...")

r1 = requests.post(creds.BASE_URL + "/initiate-handshake", json={
    "platform_name": creds.PLATFORM_NAME,
    "platform_key": creds.PLATFORM_KEY,
    "platform_secret": creds.PLATFORM_SECRET,
    "callback_url": creds.CALLBACK_URL
})

token = r1.json()["data"]["handshake_token"]
expiry = r1.json()["data"]["expires_at"]
print("Token:", token)
print("Expires at:", expiry)

print("\nStep 2: Completing handshake...")

r2 = requests.post(creds.BASE_URL + "/complete-handshake", json={
    "handshake_token": token,
    "platform_key": creds.PLATFORM_KEY
})

result = r2.json()["data"]
print("Access Token:", result["access_token"])
print("Session Expires at:", result["expires_at"])
print("\nConnected to Afya Platform successfully!")
