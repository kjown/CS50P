import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(edu|gov|com|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")