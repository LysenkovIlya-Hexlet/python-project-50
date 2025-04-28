import json


def parse_file(file_path):
    """Чтение и парсинг JSON-файла."""
    with open(file_path) as file:
        return json.load(file)