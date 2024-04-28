import csv


def load_csv_as_dict(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        return list(reader)