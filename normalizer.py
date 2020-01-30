#!/usr/bin/python3

import csv
import datetime
import os
import sys


def pacific_to_eastern_time(timestamp):
    date, time = timestamp.split(' ')
    year, month, day = list(map(int, date.split('-')))
    hours, minutes, seconds = list(map(int, time.split(':')))

    datetime_object = datetime.datetime(
        year=year, month=month, day=day, hour=hours, minute=minutes, second=seconds
    )
    datetime_object += datetime.timedelta(hours=3) # add 3 hours to get eastern time

    return str(datetime_object)

def format_date(date):
    """Convert date in to ISO-8601 format YYYY-MM-DD"""

    month, day, year = date.split('/')
    year = '20' + year # Assume the we're in the 21st century for year.
    month = month if len(month) == 2 else month.rjust(2, '0')
    day = day if len(day) == 2 else day.rjust(2, '0')
    return year + '-' + month + '-' + day

def format_time(time, time_period):
    """Convert time in to ISO-8601 format hh:mm:ss in 24-hour clock system"""

    hours, minutes, seconds = time.split(':')
    if time_period == 'AM' and hours == '12':
        return '00:' + minutes + ':' + seconds
    elif time_period == 'AM':
        return time
    elif time_period == 'PM' and hours == '12':
        return time
    else:
        return str(int(hours) + 12) + ':' + minutes + ':' + seconds

def format_timestamp(timestamp):
    date, time, time_period = timestamp.split(' ')
    date = format_date(date)
    time = format_time(time, time_period)
    formatted_timestamp = pacific_to_eastern_time(date + ' ' + time)
    return formatted_timestamp

def format_zip_code(zip_code):
    if len(zip_code) == 5:
        return zip_code
    return zip_code.rjust(5, '0')

def convert_time_to_seconds(time):
    hours, minutes, seconds = time.split(':')
    return int(hours) * 3600 + int(minutes) * 60 + float(seconds)

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
    
    input_file = open(input_file_name, encoding='utf8', errors='replace')
    input_file_reader = csv.DictReader(input_file)
    output_file = open(output_file_name, 'w', newline='')
    output_file_writer = csv.DictWriter(output_file, column_header_names)

    output_file_writer.writeheader()
    for row in input_file_reader:
        converted_foo_duration = convert_time_to_seconds(row['FooDuration'])
        converted_bar_duration = convert_time_to_seconds(row['BarDuration'])
        total_duration = converted_foo_duration + converted_bar_duration

        output_file_writer.writerow({
            'Timestamp': format_timestamp(row['Timestamp']),
            'Address': row['Address'],
            'ZIP': format_zip_code(row['ZIP']),
            'FullName': row['FullName'].upper(),
            'FooDuration': converted_foo_duration,
            'BarDuration': converted_bar_duration,
            'TotalDuration': total_duration,
            'Notes': row['Notes']
        })

    output_file.close()
    
    
normalize(sys.argv[1], sys.argv[2])