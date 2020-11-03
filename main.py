import requests, json

username = input("Insert the username: ")

x = requests.get(f"https://api.github.com/users/{username}/repos").json()

g = 0

try:
  while True:
    print(f"Repository #{g+1} > {x[g]['html_url']}")
    g += 1
except:
  print("Done!")
