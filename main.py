import requests

# Base URL of the API
base_url = "http://10.20.202.211/user/api/v1/validate/"


# Login endpoint
# login_endpoint = "login"

# User credentials
username = "kpatil"
password = "Cas@12345"

# Construct the login payload
login_payload = {"userName":"kpatil",
                "password":"Cas@1234"}
headers = {
'content-type' : 'application/json',
}

# Perform the login request
login_response = requests.post(base_url , json=login_payload)
# print(login_response)
# print("login sucsess")
# Check the response status code
# if login_response.status_code == 200:
#     # Successful login
#     response_data = login_response.json()
#     print(response_data)
#     access_token = response_data['data']['token']
#     #print(access_token)
#     print("Login successful. Access Token:", access_token)
# else:
#     print("Login failed. Status Code:", login_response.status_code)
#     print("Response:", login_response.text)


# Python code to pick a random
# word from a text file
import random
import time

# Open the file in read mode ( partner creation)
with open("D:/Partnerlist.txt", "r") as file:
		allText = file.read()
		partner = list(map(str, allText.split()))

		# print random string
		name=random.choice(partner)
		group=random.choice(partner)

Industryvertical = ["Pharmaceutical/Biotech","Telecommunication","Insurance","Healthcare","Banking & Financial Services",
					"Media & Entertainment","Logistics & Supply-chain","Others","Gaming"]
indusrty_ver= random.choice(Industryvertical)
print(indusrty_ver)








