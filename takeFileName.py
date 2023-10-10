import json
import os


def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


lang_folder_path = "./i18n"

index = 0

for files in os.listdir(lang_folder_path):
    if os.path.isfile(os.path.join(lang_folder_path, files)):
        name, extension = os.path.splitext(files)
        if name not in ["en",
                        "fr",
                        "ar",
                        "es",
                        "de",
                        "it",
                        "pt",
                        "ja",
                        "th",
                        "he",
                        "cs",]:
            print('"' + name + '"', end='')
            index += 1
            # print('INDEX' + str(index))
            # print(len(os.listdir(lang_folder_path)) - 11)
            if index == len(os.listdir(lang_folder_path)) - 11:
                print('')  # Print a new line if it's the last file
            else:
                print(',')
