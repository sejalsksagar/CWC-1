import json
import csv

def convert_to_csv():
    json_fn = 'Stock List.json'
    csv_fn = 'StockList_csv.csv'

    with open(json_fn) as json_file:
        jsondata = json.load(json_file)

    csv_file = open('StockList_csv.csv', 'w', newline='')
    csvdata = csv.writer(csv_file)

    count = 0
    for data in jsondata:
        if count == 0:
            header = data.keys()
            csvdata.writerow(header)
            count += 1
        csvdata.writerow(data.values())

    csv_file.close()