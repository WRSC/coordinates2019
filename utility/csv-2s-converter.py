#!/usr/bin/python3
# This script convert CSV-2s file to standard time-stamped csv file
# ./csv-2s-converter input_file.csv output_file.csv


import csv
import sys

file_name = sys.argv[1]
output_filename = sys.argv[2]

processed_row = []
with open(file_name, 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        processed_row.append('2019-08-26T' + row[0][:2] + ':' +
               row[0][2:4] + ':' +  row[0][4:6] + 'Z,' +
               str(float(row[1])/10000000) + ',' + 
               str(float(row[2])/10000000) + ',0,0\n' )

with open(output_filename, 'w') as f:
    csv_writer = f.writelines(processed_row)



