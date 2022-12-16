import json
import urllib.request

json_data_source = 'https://www.ncei.noaa.gov/cag/global/time-series/globe/land_ocean/1/9/1880-2022/data.json'

# with open(json_data_source, encoding='utf-8') as data:
# instead use a stream to read the file from the internet url
# usually have to call the read method of a stream
with urllib.request.urlopen(json_data_source) as json_stream:
    data = json_stream.read().decode('utf-8')  # NEW !!!
    anomalies = json.loads(data)  # loadS

print(anomalies['description'])
for year, value in anomalies['data'].items():
    year, value = int(year), float(value)
    print(f'{year} ...{value:6.2f}')

print('*'*80)
