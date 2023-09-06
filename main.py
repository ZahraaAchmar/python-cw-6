person = {
    "name": "zahraa",
    "age": 17,
    "hobbies": ["football", "building stuff", "reading"]
}
print(person["name"])
print(person["age"])

person["age"]= 18
person["country"] = "Lebanon"
print(person)
print(len(person))

person["hobbies"].append("coding")
print(person)
def check_hobbies(person):
    if len(person["hobbies"]) > 3:
        print("WOW YOU ARE AMAZING!")
check_hobbies(person)