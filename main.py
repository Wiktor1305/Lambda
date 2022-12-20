import csv
import json
import os

def handler(event, context):
    #pobranie plików .csv z eventu
    csv_files = event["csv_files"]

    #inicjalizacja listy na dane z plików .csv
    data = []

    for file in csv_files:
        with open(file, "r") as csv_file:
            reader = csv.reader(csv_file)

            for row in reader:
                color_name = row[0]
                color_hex = row[1]
                #konwersja kodu HEX na RGB
                color_rgb = tuple(int(color_hex[i:i+2], 16) for i in (1, 3, 5))

                #dodanie danych o kolorze do listy
                data.append({"name": color_name, "hex": color_hex, "rgb": color_rgb})

    #zapisanie danych do pliku .json
    with open("colors.json", "w") as json_file:
        json.dump(data, json_file)

    #zwrócenie danych o kolorach
    return data
