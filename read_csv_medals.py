import csv

# This file is a model how to read csv files with python

csv_filename = 'OlympicMedals_2020.csv'
with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    # the csv module will deal with new lines itself
    # instead of specifying them ourselves (LF, CR...)
    headers = csv_file.readline().strip('\n').split(',')
    # the first row will now be fixed because the file pointer has moved
    print(f'Column headers: {headers}')
    reader = csv.reader(csv_file)  # will return the reader object
    for row in reader:
        # the csv reader fnc returns a reader object which is iterable
        print(row)
