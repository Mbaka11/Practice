import json


def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def compare_json_keys(file1_path, file2_path):
    # Load the JSON data from the files
    json1 = load_json(file1_path)
    json2 = load_json(file2_path)

    # Get the keys from each JSON file
    keys1 = set(json1.keys())
    keys2 = set(json2.keys())

    # Find keys that are unique to each JSON file
    unique_to_file1 = keys1 - keys2
    unique_to_file2 = keys2 - keys1

    print("Keys unique to the first file (alphabetical order):")
    i = 1
    for elem in sorted(unique_to_file1):
        print(str(i) + ". " + elem)
        i += 1

    return {
        'unique_to_file1': list(unique_to_file1),
        'unique_to_file2': list(unique_to_file2)
    }


if __name__ == "__main__":
    file1_path = "en.json"  # Replace with your first JSON file path
    file2_path = "bs_BA.json"  # Replace with your second JSON file path

    result = compare_json_keys(file1_path, file2_path)
