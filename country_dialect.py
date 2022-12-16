import csv

# Learning about Sniffer

input_filename = 'country_info.txt'

with open(input_filename, encoding='utf-8', newline='') as countries_data:
    sample = ""
    for line in range(3):
        sample += countries_data.readline()
    # the following line creates a new Sniffer object and calls the
    # sniff method:
    countries_dialect = csv.Sniffer().sniff(sample)
    # change the dialect object:
    countries_dialect.skipinitialspace = True
    # go back to start of file:
    countries_data.seek(0)  # !!! return the file pointer to position
    country_reader = csv.reader(countries_data, dialect=countries_dialect)
    for row in country_reader:
        print(row)

print('+'*80)
attributes = ['delimiter',
              'doublequote',
              'escapechar',
              'lineterminator',
              'quotechar',
              'quoting',
              'skipinitialspace',
              ]

for attribute in attributes:
    # repr is useful for diagnostic information
    # repr will print out special character like new line char as '\n'
    # instead of an actual new line
    # getattr for any object
    print(f'{attribute}: {repr(getattr(countries_dialect, attribute))}')

# DISCARDED CODE
# sample = countries_data.read()  # read entire file as string
