import json
import os
# quotes = json.load(open("engiQuotes.txt"))
voiceQuotes = os.listdir("Sounds/")
token = ""
try:
    # We can't include token.txt in the repository as it is private
     with open("token.txt") as file:
        token = file.read()
except FileNotFoundError as e:
    print(e)
