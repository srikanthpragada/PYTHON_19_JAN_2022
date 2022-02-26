import requests

response = requests.get(f"https://restcountries.com/v3.1/all")
if response.status_code != 200:  # unsuccessful request
    print("Sorry! Could not get details.")
    exit()

countries = response.json()
for c in sorted(countries, key=lambda c: c['area'], reverse=True)[:10]:
    print(f"{c['name']['common']:50} {c['area']:10}")
