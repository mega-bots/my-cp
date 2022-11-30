import requests

endpoint = "https://api.assemblyai.com/v2/transcript"

json = {
  "audio_url": "https://storage.googleapis.com/bucket/b2c31290d9d8.wav"
}

headers = {
  "Authorization": "c2a41970d9d811ec9d640242ac12",
  "Content-Type": "application/json"
}

response = requests.post(endpoint, json=json, headers=headers)
vars(response)
