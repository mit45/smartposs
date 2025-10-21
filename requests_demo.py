import requests

# 1. Örnek: GET isteği
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print("GET isteği sonucu:")
print(response.status_code)
print(response.json())

# 2. Örnek: POST isteği
new_post = {
    "title": "Ümit'in Denemesi",
    "body": "Bu, ilk POST isteğimizdir!",
    "userId": 1
}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
print("\nPOST isteği sonucu:")
print(response.status_code)
print(response.json())
