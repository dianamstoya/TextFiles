import csv

countries_filename = 'country_info.txt'
dialect = csv.excel
dialect.delimiter = '|'

countries = {}
with open(countries_filename, encoding='utf-8', newline='') as country_file:
    # Get the column headings from the first line of the file
    headings = country_file.readline().strip('\n').split(dialect.delimiter)
    for index, heading in enumerate(headings):
        headings[index] = heading.casefold()

    dict_reader = csv.DictReader(country_file, dialect=dialect, fieldnames=headings)  # delimiter='|'
    for row in dict_reader:
        countries[row['country'].casefold()] = row
        countries[row['cc'].casefold()] = row

# print(countries)
while True:
    country_input = input("Enter a country name: ")
    country_key = country_input.casefold()
    if country_key in countries:
        print(f"The capital of {country_input} is {countries[country_key]['capital']}.")
    elif country_key == 'quit':
        break
    else:
        print(f"Country {country_input} not found.")

# DISCARDED CODE
# using sniffer
#     sample = ""
#     for line in range(3):
#         sample += country_file.readline()
#     dialect = csv.Sniffer().sniff(sample)
#     country_file.seek(0)
