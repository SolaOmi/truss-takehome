#!/usr/bin/python3

import csv
import os
import sys


def is_csv_file(file):
    return file.endswith('csv')
    
def normalize(input_file_name, output_file_name):
    if not is_csv_file(input_file_name) or not is_csv_file(output_file_name):
        print("Please provide csv files as arguments!")
        return None
        
    if not os.path.isfile(input_file_name):
        print("Please make sure your input file exists.")
        return None
        
    input_file = open(input_file_name)
    header_names = [
        'Timestamp', 'Address', 'ZIP', 'FullName', 'FooDuration', 'BarDuration',
        'TotalDuration', 'Notes'
    ]
    input_file_reader = csv.DictReader(input_file, header_names)
    
    for row in input_file_reader:
        print(row['Timestamp'], row['Address'], row['ZIP'])
    
    
normalize(sys.argv[1], sys.argv[2])