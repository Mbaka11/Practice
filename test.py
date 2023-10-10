import json

# Function to read a JSON file and return its content as a dictionary


def read_json_file(file_path):
    with open(file_path, 'r') as json_file:
        return json.load(json_file)


def find_attributes_with_same_key(json1, json2):
    shared_keys = set(json1.keys()) & set(json2.keys())
    return shared_keys


def find_attributes_with_same_value(json1, json2):
    shared_attributes = []

    for key1, value1 in json1.items():
        for key2, value2 in json2.items():
            if value1 == value2:
                shared_attributes.append((key1 + "/" + key2, value1))

    return shared_attributes


# File paths for the two JSON files you want to compare
file1_path = 'en2.json'
file2_path = 'en.json'

# Read the JSON files
json1 = read_json_file(file1_path)
json2 = read_json_file(file2_path)

# Find shared attributes
shared_keys = find_attributes_with_same_key(json1, json2)

shared_values = find_attributes_with_same_value(json1, json2)

# Print the results
print("Same Keys:", shared_keys)
print("---------------------------------------------" + "\n")
print("Same Values:", shared_values)
