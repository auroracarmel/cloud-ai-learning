description = input("Describe your request: ")
request = {"name": "Aurora", "description": description}

if request["description"].strip() == "":
    print("Missing description")
else:
    print("Description supplied")
    print("Request:", request["description"])

    if "urgent" in request["description"].lower():
        print("Flag for priority review")