import json

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]
}
'''
#load a json string into python object
data = json.loads(people_string)
print(data)

#type of data
print("-"*40)
print(f"Type of python object for data variable is a {type(data)}")
print("-"*40)
print(f"Type of python object for data ['people'] is a {type(data['people'])}") #can't use "" twice because throw out error

#access list object in people
print("-"*40)
print("List of objects in the people key:")
for person in data["people"]:
    print(person)

#access names in object: try "name", "phone", "emails", "has_license"
print("-"*40)
print("Dictionary of key values in objects:")
for person in data["people"]:
    print(person["name"])
    print(person["phone"])







