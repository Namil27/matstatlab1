import csv
import os


def parse_csv():
    file_path = os.path.abspath('funcs/cars93.csv')
    data = []

    # Открываем файл для чтения
    with open(file_path, mode='r', encoding='utf-8') as file:
        # Создаем объект reader для чтения CSV
        csv_reader = csv.reader(file)

        # Читаем заголовки (первую строку)
        headers = next(csv_reader)

        # Читаем остальные строки
        for row in csv_reader:
            # Создаем словарь для каждой строки
            row_data = {}
            for i, header in enumerate(headers):
                row_data[header] = row[i]
            data.append(row_data)

    return data
