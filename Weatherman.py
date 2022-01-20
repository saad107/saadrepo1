import os
from os import path
import argparse
import sys
from csv import DictReader
from datetime import datetime
from enum import Enum


class Colors(Enum):
    White = "\033[37m"
    Red = "\033[31m"
    Blue = "\033[34m"


def run_weather_man_month(year, month):
    file_name = make_file_name(year, month)
    maximum_temperatures, minimum_temperatures, mean_humidity_values = read_weather_files(file_name)
    maximum_temperature, minimum_temperature, average_humidity = \
        calculate_average_temperature(maximum_temperatures, minimum_temperatures, mean_humidity_values)
    display_average_temperatures(maximum_temperature, minimum_temperature, average_humidity)


def make_file_name(year, month):
    file_name = ''
    for file in os.listdir('.'):
        if year in file and month in file:
            file_name = file
    if file_name == '':
        print('File not found')
        sys.exit()
    else:
        return file_name


def read_weather_files(file_name):
    if path.exists(file_name):
        with open(file_name, 'r') as file:
            csv_reader = DictReader(file)
            maximum_temperatures = []
            minimum_temperatures = []
            mean_humidity_values = []
            for row in csv_reader:
                maximum_temperatures.append(row['Max TemperatureC'])
                minimum_temperatures.append(row['Min TemperatureC'])
                mean_humidity_values.append(row[' Mean Humidity'])
        return maximum_temperatures, minimum_temperatures, mean_humidity_values
    else:
        print(f"{file_name} 'this file does not exists'")


def calculate_average_temperature(maximum_temperatures, minimum_temperatures, mean_humidity_values):
    maximum_average_temperature = calculate_average(maximum_temperatures)
    minimum_average_temperature = calculate_average(minimum_temperatures)
    average_humidity = calculate_average(mean_humidity_values)
    return maximum_average_temperature, minimum_average_temperature, average_humidity


def calculate_average(temperature_values):
    total = 0
    count = 0
    for iterator in range(0, len(temperature_values)):
        if temperature_values[iterator] != '':
            total = total + float(temperature_values[iterator])
            count += 1
    return total / count


def display_average_temperatures(maximum_average_temperature, minimum_average_temperature,
                                 humidity_average):
    print(f'Average Highest Temperature : {maximum_average_temperature}C')
    print(f'Average Lowest Temperature : {minimum_average_temperature}C')
    print(f'Average Humidity : {humidity_average}%')


def run_weatherman_month_bar_charts(year, month):
    file_name = make_file_name(year, month)
    maximum_temperatures, minimum_temperatures = read_weather_files_for_bar_charts(file_name)
    print_bar_chart(maximum_temperatures, minimum_temperatures)


def read_weather_files_for_bar_charts(file_name):
    if path.exists(file_name):
        with open(file_name, 'r') as file:
            csv_reader = DictReader(file)
            maximum_temperatures = []
            minimum_temperatures = []
            for row in csv_reader:
                maximum_temperatures.append(row['Max TemperatureC'])
                minimum_temperatures.append(row['Min TemperatureC'])
        return maximum_temperatures, minimum_temperatures
    else:
        print(f"{file_name} 'this file does not exists'")


def print_bar_chart(maximum_values, minimum_values):
    display_bar_charts(maximum_values, minimum_values)

    display_horizontal_bar_charts(maximum_values, minimum_values)


def display_bar_charts(maximum_temperature_values, minimum_temperature_values):
    for iterator in range(0, len(minimum_temperature_values)):
        if maximum_temperature_values[iterator] == '':
            print('', end='')
        else:
            print(Colors.White.value, iterator + 1, end='')
            display_colored_barchart(float(maximum_temperature_values[iterator]), Colors.Red.value)
            maximum_temperature = f'{int(maximum_temperature_values[iterator])}C'
            print(Colors.White.value, maximum_temperature, end='')
            print('')
            print(Colors.White.value, iterator + 1, end='')
            display_colored_barchart(float(minimum_temperature_values[iterator]), Colors.Blue.value)
            minimum_temperature = f'{int(minimum_temperature_values[iterator])}C'
            print(Colors.White.value, minimum_temperature, end='')
            print('')


def display_horizontal_bar_charts(maximum_temperature_values, minimum_temperature_values):
    for iterator in range(0, len(minimum_temperature_values) - 1):
        if maximum_temperature_values[iterator] == '':
            print('', end='')
        else:
            print(iterator + 1, end='')
            display_colored_barchart(float(maximum_temperature_values[iterator]), Colors.Red.value)
            display_colored_barchart(float(minimum_temperature_values[iterator]), Colors.Blue.value)
            temperature_range = f'{int(maximum_temperature_values[iterator])}C-' \
                                f''f'{int(minimum_temperature_values[iterator])}C'
            print(Colors.White.value, temperature_range, end='')
            print('')


def display_colored_barchart(number, color):
    number_of_stars = int(number) + 1
    for iterator in range(1, number_of_stars):
        print(color + '+', end='')


def run_weather_man_year(year):
    maximum_temperatures, minimum_temperatures, mean_humidity, \
        maximum_temperatures_dates, minimum_temperatures_dates, mean_humidity_dates\
        = read_files_year(year)

    maximum_temperatures, minimum_temperatures, mean_humidity, maximum_temperatures_dates, \
        minimum_temperatures_dates, mean_humidity_dates = \
        calculate_results(maximum_temperatures, minimum_temperatures, mean_humidity,
                          maximum_temperatures_dates, minimum_temperatures_dates, mean_humidity_dates)
    display_results(maximum_temperatures, minimum_temperatures, mean_humidity,
                    maximum_temperatures_dates, minimum_temperatures_dates, mean_humidity_dates)


def read_files_year(year):
    maximum_temperatures = []
    minimum_temperatures = []
    minimum_temperature_dates = []
    maximum_temperature_dates = []
    mean_humidity = []
    mean_humidity_dates = []
    file_collection = get_file_collection(year)
    for iterator in file_collection:
        if path.exists(iterator):
            max_temperature_values, min_temperature_values, mean_humidity_values, date_reading = \
                read_temperature_values(iterator)

            index_max = find_maximum_temperature_index(max_temperature_values)
            maximum_temperature = max_temperature_values[index_max]
            maximum_temperatures.append(maximum_temperature)
            maximum_temperature_dates.append(get_date(date_reading, index_max))

            index_min = find_minimum_temperature_index(min_temperature_values)
            minimum_temperature = min_temperature_values[index_min]
            minimum_temperatures.append(minimum_temperature)
            minimum_temperature_dates.append(get_date(date_reading, index_min))

            index_mean = find_maximum_temperature_index(mean_humidity_values)
            mean_humidity1 = mean_humidity_values[index_max]
            mean_humidity.append(mean_humidity1)
            mean_humidity_dates.append(get_date(date_reading, index_mean))
    return maximum_temperatures, minimum_temperatures, mean_humidity, \
        maximum_temperature_dates, minimum_temperature_dates, mean_humidity_dates


def get_file_collection(year):
    file_collection = []
    for file in os.listdir('.'):
        if year in file:
            file_collection.append(file)
    size = len(file_collection)
    if size == 0:
        print("Files not found")
        sys.exit()
    else:
        return file_collection


def get_date(date_values, index):
    return date_values[index]


def read_temperature_values(file_name):
    max_temperature_values = []
    min_temperature_values = []
    mean_humidity_values = []
    with open(file_name, 'r') as file:
        csv_reader = DictReader(file)
        date_reading = []
        for row in csv_reader:
            max_temperature_values.append(row['Max TemperatureC'])
            min_temperature_values.append(row['Min TemperatureC'])
            mean_humidity_values.append(row[' Mean Humidity'])
            date_reading.append(row['PKT'])

    return max_temperature_values, min_temperature_values, mean_humidity_values, date_reading


def calculate_results(maximum_values, minimum_values, humidity_reading,
                      maximum_date_values, minimum_date_values, date_values_humidity):
    maximum_temperature = maximum_values[find_maximum_temperature_index(maximum_values)]
    minimum_temperature = minimum_values[find_minimum_temperature_index(minimum_values)]
    maximum_humidity = humidity_reading[find_maximum_temperature_index(humidity_reading)]

    maximum_temperature_date = maximum_date_values[find_maximum_temperature_index(maximum_values)]
    minimum_date_value = minimum_date_values[find_minimum_temperature_index(minimum_values)]
    mean_humidity_date = date_values_humidity[find_maximum_temperature_index(humidity_reading)]

    maximum_temperature_date = change_date_format(maximum_temperature_date)
    minimum_date_value = change_date_format(minimum_date_value)
    mean_humidity_date = change_date_format(mean_humidity_date)
    return maximum_temperature, maximum_temperature_date, \
        minimum_temperature, minimum_date_value, maximum_humidity, mean_humidity_date


def find_maximum_temperature_index(temperature_values):
    maximum1 = 0
    maximum_temperature_index = 0
    for iterator in range(0, len(temperature_values)):
        if temperature_values[iterator] != '':
            if float(temperature_values[iterator]) >= maximum1:
                maximum1 = float(temperature_values[iterator])
                maximum_temperature_index = iterator
    return maximum_temperature_index


def find_minimum_temperature_index(temperature_values):
    minimum1 = float(temperature_values[0])
    minimum_temperature_index = 0
    for iterator in range(1, len(temperature_values)):
        if temperature_values[iterator] != '':
            if float(temperature_values[iterator]) < minimum1:
                minimum1 = float(temperature_values[iterator])
                minimum_temperature_index = iterator
    return minimum_temperature_index


def display_results(maximum_temperature, maximum_date, minimum_temperature, minimum_date,
                    mean_humidity, mean_humidity_date):
    maximum_detail = f'Max temperature is {maximum_temperature}C on 'f'{maximum_date}'
    minimum_detail = f'Min temperature is {minimum_temperature}C on 'f'{minimum_date}'
    mean_humidity_detail = f'Max Humidity is {mean_humidity}% on 'f'{mean_humidity_date}'
    print(maximum_detail)
    print(minimum_detail)
    print(mean_humidity_detail)


def change_date_format(date):
    year, month, day = date.split('-')
    datetime_object = datetime.strptime(month, "%m")
    month_name = datetime_object.strftime("%b")
    new_date = f'{day}' + f' {month_name} '
    return new_date


def find_month_name(number):
    try:
        datetime_object = datetime.strptime(number, "%m")
        month_name = datetime_object.strftime("%b")
        return month_name
    except ValueError:
        print('Wrong Input')
        sys.exit()


def run_weather_man(args):
    if args.operator == 'e':
        if len(args.year) == 4:
            run_weather_man_year(args.year)
        else:
            print('Wrong Input')
    else:
        year = args.year[:4]
        month = args.year[5:]
        month = find_month_name(month)
        if args.operator == 'a':
            run_weather_man_month(year, month)
        elif args.operator == 'c':
            run_weatherman_month_bar_charts(year, month)
        else:
            print('Wrong Input')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('operator', action='store', default='')
    parser.add_argument('year', action='store', default='')
    arguments = parser.parse_args()
    run_weather_man(arguments)

