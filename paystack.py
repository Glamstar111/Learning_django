import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

sk = os.getenv("PAYSTACK_SECRET_KEY")

url ="https://api.paystack.co/transaction/initialize"

headers = {
    "Autorization": f"Bearer {sk}",
    "Content-Type": "application/json"
}

data = {"email": "customer@email.com", "amount": 500000 * 100}

response = requests.post(url,data=json.dumps(data), headers=headers)
print(response.json())