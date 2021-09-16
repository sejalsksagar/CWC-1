import csv


def find_symbol(x):
    read_fn = "StockList_csv.csv"
    write_fn = "Symbols.csv"

    count = 0
    header = []
    rows = []

    # reading csv file
    with open(read_fn, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)

        for row in csvreader:
            if x in row[4]:
                rows.append(row)
                count += 1

    # writing to csv file
    with open(write_fn, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)
        csvwriter.writerows(rows)

    return count