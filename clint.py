import requests

url = "http://127.0.0.1:5000/ask"

user = input("Enter your question: ")
questions = {"question": user}
response = requests.post(url, json=questions)
print("Response:", response.json()["answer"])