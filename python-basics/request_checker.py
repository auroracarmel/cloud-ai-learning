request = {"name": "Aurora", "description": ""}


if request["description"].strip() == "":
    print("Missing description")
else:
    print("Description supplied")