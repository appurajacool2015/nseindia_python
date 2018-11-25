## Prior running - 
## pip install nsetools --update

from nsetools import Nse

nse = Nse()

quotes_dict = nse.get_quote('infy')

# Get dict key list
header_field_names_list = list(quotes_dict.keys())
# Get rows dict list
rows_dict_list = list(quotes_dict.values())


 # Open csv file with write permission.
csv_file_object = open('D:\\Codes\\Python\\practise\\nseindia.csv', 'w')

# import csv

# # Create a csv.DictWriter object with the target csv file and specified header field names list..
# csv_dict_file_writer = csv.DictWriter(csv_file_object, fieldnames=header_field_names_list)

# # Write csv file header field names.
# csv_dict_file_writer.writeheader()

# # Get rows dict list
# rows_dict_list = list(quotes_dict.values())

# # Loop in the row list.
# for row_dict in rows_dict_list:
# 	#Write each row dict data to the csv file.
#     csv_dict_file_writer.writerow(row_dict)

from pprint import pprint
pprint (quotes_dict)

import json
import csv

quotes_str = json.dumps(quotes_dict)
nse_json = json.loads(quotes_str)

# print (nse_json['symbol'])

# symbol = nse_json['symbol']
# day_low_price = nse_json['day_low']
# day_high_price = nse_json['day_high']


#from pprint import pprint
csv_writer = csv.writer(open('D:\\Codes\\Python\\practise\\nseindia.csv','w+'))

csv_writer.writerow(header_field_names_list)
# csv_writer.writerows([rows_dict_list])

for row in rows_dict_list:
	csv_writer.writerow(repr(row['companyName'])

# for k, v in quotes_dict.items: 
# 	f.writerow()

