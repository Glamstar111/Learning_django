import requests

response = requests.get("https://dummyjson.com/products")
products = response.json