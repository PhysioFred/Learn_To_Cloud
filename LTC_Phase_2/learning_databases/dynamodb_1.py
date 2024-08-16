#First time Dynamodb/nosql database
#value of key is a dictionary. Dict = key-value pair. Key = data type.
#value needs to be a string as sends across the network to Dynamodb, then it will convert to a number
#future project, creat a table loaded from a seperate json file


import boto3

client = boto3.client("dynamodb")

#TODO: Get Item
response = client.get_item(
    TableName="Students", 
    Key={"student_id": {"N": "69"}},
    AttributesToGet=["student_id", "age", "name", "gender"],
)
print(response)

#TODO: Delete Item
# response = client.delete_item(
#     TableName="Students",
#     Key={"student_id": {"N":"1"}},
# )

#TODO: Put Item
# response = client.put_item(
#     TableName="Students",
#     Item={"student_id": {"N":"69"}, "name": {"S": "Matilda"}, "age": {"N":"32"}, "gender": {"S": "Female"}},
# )


#TODO: Update Item
reponse = client.update_item(
    TableName="Students",
    Key={"student_id": {"N": "2"}},
    AttributeUpdates={"gender": {"Value": {"S": "Female"}, "Action": "PUT"}},
)


