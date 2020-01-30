#!/usr/bin/python3

import csv
import os
import sys


def format_zip_code(zip_code):
    if len(zip_code) == 5:
        return zip_code
    return zip_code.rjust(5, '0')

def is_csv_file(file):
    return file.endswith('csv')
    
def normalize(input_file_name, output_file_name):
    if not is_csv_file(input_file_name) or not is_csv_file(output_file_name):
        print("Please provide csv files as arguments!")
        return None
        
    if not os.path.isfile(input_file_name):
        print("Please make sure your input file exists.")
        return None
        
    column_header_names = [
        'Timestamp', 'Address', 'ZIP', 'FullName', 'FooDuration', 'BarDuration',
        'TotalDuration', 'Notes'
    ]
    
    input_file = open(input_file_name)
    input_file_reader = csv.DictReader(input_file, column_header_names)
    output_file = open(output_file_name, 'w', newline='')
    output_file_writer = csv.DictWriter(output_file, column_header_names)

    for row in input_file_reader:
        output_file_writer.writerow({
            'Timestamp': row['Timestamp'],
            'Address': row['Address'],
            'ZIP': format_zip_code(row['ZIP']),
            'FullName': row['FullName'],
            'FooDuration': row['FooDuration'],
            'BarDuration': row['BarDuration'],
            'TotalDuration': row['TotalDuration'],
            'Notes': row['Notes']
        })

    output_file.close()
    
    
normalize(sys.argv[1], sys.argv[2])