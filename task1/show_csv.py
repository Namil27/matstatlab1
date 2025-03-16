from funcs.csv_parser import parse_csv


raw_list = parse_csv()

for raw in raw_list:
    print(raw)