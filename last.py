import csv

my_headers = ['Name', 'EID', 'DOMAIN']
my_values = [
    ['Akil', 8901, 'SUP'],
    ['John', 7812, 'DB'],
    ['Zoya', 8034, 'SUP'],
    ['Asha', 1233, 'DEV']
]
filename = 'employeedata.csv'

with open(filename, 'w', newline='') as myfile:
    writer = csv.writer(myfile)
    writer.writerow(my_headers)
    writer.writerows(my_values)
