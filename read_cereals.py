import csv

csv_filename = 'cereal_grains.csv'
with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    # if csv file has strings quoted
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)
