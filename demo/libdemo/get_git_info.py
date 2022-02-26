import requests

USER = "srikanthpragada"
#USER = "scottallen"
response = requests.get(f"https://api.github.com/users/{USER}")
if response.status_code != 200:  # unsuccessful request
    print("Sorry! Could not get details.")
    exit()

details = response.json()
print(f"Name     : {details['name']}")
print(f"Company  : {details['company']}")
print(f"Location : {details['location']}")