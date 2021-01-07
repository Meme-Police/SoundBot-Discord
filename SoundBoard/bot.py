import json
import os
# quotes = json.load(open("engiQuotes.txt"))
voiceQuotes = os.listdir("Sounds/")
token = ""
try:
    # We can't include shaxxToken.txt in the repository as it is private
     with open("engiToken.txt") as file:
        token = file.read()
except FileNotFoundError as e:
    print(e)
