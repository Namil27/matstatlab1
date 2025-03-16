from funcs.csv_parser import parse_csv


raw_list = parse_csv()
popularity = {}

for raw in raw_list:
    type = raw["Type"]

    if raw["Type"] not in popularity.keys():
        popularity[type] = 1
        continue
    popularity[type] += 1

print(popularity)