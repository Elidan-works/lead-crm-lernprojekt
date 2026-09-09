import requests

antwort = requests.get("https://api.github.com")

print(antwort.status_code)

daten = antwort.json()
print(daten["emojis_url"])

header_daten = {"Authorization": "Bearer mein-test-key"}
antwort2 = requests.get("https://httpbin.org/headers", headers=header_daten)

print(antwort2.json())
