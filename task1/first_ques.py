from funcs.csv_parser import parse_csv


# Получаем список, в каждом элементе словарь с данными одной строки
raw_list = parse_csv()
types_set = set()

for raw in raw_list:
    types_set.add(raw["Type"])

print(types_set)
