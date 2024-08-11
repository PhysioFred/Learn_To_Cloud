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

data = json.loads(people_string)
print(data)

#type of data
print("-"*40)
print(f"Type of python object for data variable is a {type(data)}")
print("-"*40)
print(f"Type of python object for data ['people'] is a {type(data['people'])}") #can't use "" twice because throw out error

#access list
print("-"*40)
for person in data["people"]:
    print(person)






