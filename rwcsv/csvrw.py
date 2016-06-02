#!/usr/bin/python3

import csv

csvfile = 'zoznam.csv'


#with open('zoznam.csv', 'rb') as csvfile:
#    phonesreader = csv.reader(csvfile, delimiter=',', quotechar='|')
#    for row in phonesreader:
#         print ', '.join(row)



# define read function 
def read(csvfile):
	with open(csvfile, 'r+', newline='') as csv_file:
		reader = csv.reader(csv_file, delimiter=',')
		return [row for row in reader]

# define write function
def write(csvfile):
	with open(csvfile, 'w+', newline='') as csv_file:
		writer = csv.writer(csv_file, delimiter=',')
		for row in rows: 
			writer.writerow(row)

# define raw test
#def raw_test():
#	columns = int(input("How many columns do you want to write? "))
#	input_rows = []
#	keep_going = True
#	while kep_going:
#		input_rows.append(input("column (): ".format(1 + 1)) for i in range(0, columns)])
#		ui_keep_going = input("continue? (y/N): ")
#	keep_going = False
#
#	print(str(input_rows))
#	write('raw.csv', input_rows)
#	print(str(written_value))
#
#raw_test() 


