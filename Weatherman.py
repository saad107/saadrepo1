import argparse
from csv import DictReader
from datetime import datetime
from os import path

White = "\033[37m"
Red = "\033[31m"
Blue = "\033[34m"


def run_weather_man_month(year, month, operator):
    file_name = f'Murree_weather_{year}_{month}.txt'
    read_weather_files(file_name, operator)


def read_weather_files(file_name, operator):
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
        calculate_monthly_results(maximum_temperatures, minimum_temperatures,
                                  mean_humidity_values, operator)
    else:
        print(f"{file_name} 'this file does not exists'")


def calculate_monthly_results(maximum_temperatures, minimum_temperatures,
                              mean_humidity_values, operator):
    if operator == '-a':
        calculate_average_temperature(maximum_temperatures,
                                      minimum_temperatures,
                                      mean_humidity_values)
    elif operator == '-c':
        make_bar_chart(maximum_temperatures, minimum_temperatures)


def calculate_average_temperature(maximum_temperatures, minimum_temperatures, mean_humidity_values):
    maximum_average_temperature = calculate_average(maximum_temperatures)
    minimum_average_temperature = calculate_average(minimum_temperatures)
    average_humidity = calculate_average(mean_humidity_values)

    display_average_temperatures(maximum_average_temperature,
                                 minimum_average_temperature,
                                 average_humidity)


def make_bar_chart(maximum_values, minimum_values):

    display_bar_charts(maximum_values, minimum_values)

    display_horizontal_bar_charts(maximum_values, minimum_values)


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


def display_bar_charts(maximum_temperature_values, minimum_temperature_values):
    for iterator in range(0, len(minimum_temperature_values)):
        if maximum_temperature_values[iterator] == '':
            print('', end='')
        else:
            print(White, iterator + 1, end='')
            display_colored_barchart(float(maximum_temperature_values[iterator]), Red)
            print(White, f'{int(maximum_temperature_values[iterator])}C', end='')
            print('')
            print(White, iterator + 1, end='')
            display_colored_barchart(float(minimum_temperature_values[iterator]), Blue)
            print(White, f'{int(minimum_temperature_values[iterator])}C', end='')
            print('')


def display_horizontal_bar_charts(maximum_temperature_values, minimum_temperature_values):
    for iterator in range(0, len(minimum_temperature_values)-1):
        if maximum_temperature_values[iterator] == '':
            print('', end='')
        else:
            print(iterator+1, end='')
            display_colored_barchart(float(maximum_temperature_values[iterator]), Red)
            display_colored_barchart(float(minimum_temperature_values[iterator]), Blue)
            print(White, f'{int(maximum_temperature_values[iterator])}C-'
                  f'{int(minimum_temperature_values[iterator])}C', end='')
            print('')


def display_colored_barchart(number, color):
    number_of_stars = int(number) + 1
    for iterator in range(1, number_of_stars):
        print(color + '+', end='')


# For year

def make_filename(year, number):
    month_number = str(number)
    datetime_object = datetime.strptime(month_number, "%m")
    month_name = datetime_object.strftime("%b")
    file_name = f'Murree_weather_{year}_{month_name}.txt'
    return file_name


def run_weather_man_year(year):
    maximum_temperatures = []
    minimum_temperatures = []
    minimum_temperature_dates = []
    maximum_temperature_dates = []
    mean_humidity = []
    mean_humidity_dates = []                 # I need these variables in and after the for loop
    for iterator in range(1, 13):
        file_name = make_filename(year, iterator)
        if path.exists(file_name):
            max_temperature_values, min_temperature_values, mean_humidity_values, date_reading = \
                    make_temperature_values(file_name)     # 1st function
        # we are calculating max month temp of every month in every iteration
            index_max = calculate_maximum_temperature(max_temperature_values)
            maximum_temperature = max_temperature_values[index_max]
            maximum_temperatures.append(maximum_temperature)
            maximum_temperature_dates.append(calculate_date(date_reading, index_max))
        # minimum
            index_min = calculate_minimum_temperature(min_temperature_values)
            minimum_temperature = min_temperature_values[index_min]
            minimum_temperatures.append(minimum_temperature)
            minimum_temperature_dates.append(calculate_date(date_reading, index_min))
        # humidity
            index_mean = calculate_maximum_temperature(mean_humidity_values)
            mean_humidity1 = mean_humidity_values[index_max]
            mean_humidity.append(mean_humidity1)
            mean_humidity_dates.append(calculate_date(date_reading, index_mean))
    calculate_results(maximum_temperatures, maximum_temperature_dates,
                      minimum_temperatures, minimum_temperature_dates,
                      mean_humidity, mean_humidity_dates)             # 2nd function

# 1st function


def calculate_date(date_values, index):
    return date_values[index]


def make_temperature_values(file_name):
    with open(file_name, 'r') as file:
        csv_reader = DictReader(file)
        date_reading = []
        max_temperature_values = []
        min_temperature_values = []
        mean_humidity_values = []
        for row in csv_reader:
            max_temperature_values.append(row['Max TemperatureC'])
            min_temperature_values.append(row['Min TemperatureC'])
            mean_humidity_values.append(row[' Mean Humidity'])
            date_reading.append(row['PKT'])

    return max_temperature_values, min_temperature_values, mean_humidity_values, date_reading


# 2nd function

def calculate_results(maximum_values, maximum_date_values,
                      minimum_values, minimum_date_values,
                      humidity_reading, date_values_humidity):

    maximum_temperature = maximum_values[calculate_maximum_temperature(maximum_values)]
    minimum_temperature = minimum_values[calculate_minimum_temperature(minimum_values)]
    maximum_humidity = humidity_reading[calculate_maximum_temperature(humidity_reading)]

    maximum_temperature_date = maximum_date_values[calculate_maximum_temperature(maximum_values)]
    minimum_date_value = minimum_date_values[calculate_maximum_temperature(minimum_values)]
    mean_humidity_date = date_values_humidity[calculate_maximum_temperature(humidity_reading)]

    display_results(maximum_temperature, maximum_temperature_date,
                    minimum_temperature, minimum_date_value,
                    maximum_humidity, mean_humidity_date)


def calculate_maximum_temperature(temperature_values):
    maximum1 = 0
    maximum2 = 0
    for iterator in range(0, len(temperature_values)):
        if temperature_values[iterator] != '':
            if float(temperature_values[iterator]) >= maximum1:
                maximum1 = float(temperature_values[iterator])
                maximum2 = iterator
            else:
                temperature_values[iterator] = temperature_values[iterator]
    return maximum2


def calculate_minimum_temperature(temperature_values):
    minimum1 = float(temperature_values[0])
    minimum2 = 0
    for iterator in range(1, len(temperature_values)):
        if temperature_values[iterator] != '':
            if float(temperature_values[iterator]) < minimum1:
                minimum1 = float(temperature_values[iterator])
                minimum2 = iterator
            else:
                minimum1 = minimum1
    return minimum2


def display_results(maximum_temperature, maximum_date, minimum_temperature, minimum_date,
                    mean_humidity, mean_humidity_date):
    print(f'Max temperature is {maximum_temperature}C on 'f'{change_date_format(maximum_date)}')
    print(f'Min temperature is {minimum_temperature}C on 'f'{change_date_format(minimum_date)}')
    print(f'Max Humidity is {mean_humidity}% on 'f'{change_date_format(mean_humidity_date)}')


def change_date_format(date):
    date_format = date.split('-')
    month_number = date_format[1]
    datetime_object = datetime.strptime(month_number, "%m")
    month_name = datetime_object.strftime("%b")
    new_date = f'{date_format[2]}' + f' {month_name} '
    return new_date


def find_month_name(number):
    datetime_object = datetime.strptime(number, "%m")
    month_name = datetime_object.strftime("%b")
    return month_name


def run_weather_man(argument):
    if argument.year != '':
        year = argument.year.split('/')
        if len(year) == 1:
            run_weather_man_year(argument.year)
            print('')
        else:
            print('Wrong Input')
    if argument.year_month != '':
        year_charts = argument.year_month.split('/')
        if len(year_charts) == 2:
            run_weather_man_month(year_charts[0], find_month_name(year_charts[1]), '-c')
            print('')
        else:
            print('Wrong Input')
    if arguments.year_and_month != '':
        year_month = argument.year_and_month.split('/')
        if len(year_month) == 2:
            run_weather_man_month(year_month[0], find_month_name(year_month[1]), '-a')
            print('')
        else:
            print('Wrong Input')

# Main


if __name__ == '__main__':
    White = "\033[37m"
    parser = argparse.ArgumentParser()

    parser.add_argument('-e', '--year', action='store', default='')
    parser.add_argument('-c', '--year_month', action='store', default='')
    parser.add_argument('-a', '--year_and_month', action='store', default='')
    arguments = parser.parse_args()
    run_weather_man(arguments)

