import csv
import pandas as pd

my_headers = ['Name', 'EID', 'DOMAIN']
my_values = [
    ['Akil', 8901, 'SUP'],
    ['John', 7812, 'DB'],
    ['Zoya', 8034, 'SUP'],
    ['Asha', 1233, 'DEV']
]
# filename = 'employeedata.csv'
#
# with open(filename, 'w', newline='') as myfile:  # using csv
#     writer = csv.writer(myfile)
#     writer.writerow(my_headers)
#     writer.writerows(my_values)

df = pd.DataFrame(my_values, columns=my_headers)  # using pandas

df.to_csv('employeedata.csv', index=False)

df.loc[0, 'Name'] = 'Akhil'

df.to_csv('employeedata.csv', index=False)
