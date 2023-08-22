import re

url = input("URL: ").strip()

matches := re.search(r"^htts?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print("Username: ", matches.group(1))