import json

cities = {
    "pune": 10_000,
    "Mumbai": 20_000,
    "Bengluru": 7_000
}

with open("cities.json", "w") as f:
    json.dump(cities, f, indent = True)

with open("cities.json", "r") as f:
    data = json.load(f)

print(data) 
new = {"Hyderabad": 9_000}
data.update(new)

with open("cities.json", "w") as f:
    json.dump(data, f, indent = True)

# with open("cities.json", "r") as f:
#     data = json.load(f)    
#     print(data)
