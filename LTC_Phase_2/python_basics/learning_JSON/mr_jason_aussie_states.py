import json 
import os

os.chdir("/home/fredunix/Fred/learntocloud/LTC_Phase_2/python_basics/learning_JSON")

with open("aussie_states.json") as f:
    data = json.load(f)
    print("-"*40)
    print(data)
    print("-"*40)

for state in data["states"]:
    print(f"{state['name']} abbreviated to: {state['abbreviation']}")
    print(state['flora'], state['fauna'])
    print()
    
for state in data["states"]:
    del state['area_code']

#show area code key value has been deleted
print(data) #if you indent this code within the for loop above, then it will print out the data variable everytime it runs the loop

with open("new_aussie_states.json", "w") as f:
    json.dump(data, f, indent=2)

