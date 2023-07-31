import requests

print("Welcome to Jordan's flight club.\nWe find the best flight deals and email you.")
first_name = input("What's your first name? ")
last_name = input("What's your last name? ")
email_1 = input("What's your email? ")
email_2 = input("Type your email again. ")

if email_1 != email_2:
    try_again = True
    while try_again:
        print("Your emails don't match. Please try again.")
        email_1 = input("What's your email? ")
        email_2 = input("Type your email again. ")
        if email_1 == email_2:
            break

BEARER = "fsdfsdf7s8f7sf7s8fsfsf"
sheet_endpoint = "https://api.sheety.co/5d483247b4639d3684b969807cdb3de9/flightDeals/users"

body = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email_1,
    }
}

headers = {
    "Authorization": f"Bearer {BEARER}",
    "Content-Type": "application/json",
}

response = requests.post(url=sheet_endpoint, headers=headers, json=body)
result = response.json()
print(result)