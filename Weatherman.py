import os
import sys


def weather_month(year, month, calculate):
    file_name = ''
    file_reading = os.listdir('.')
    for item in file_reading:
        if year in item and month in item:  # given year or month
            file_name = item
    make_month_lists(file_name, calculate)


def make_month_lists(file_name, calculate):
    with open(file_name, 'r') as file:
        size_of_the_file = file_size(file_name)
        date_reading = []
        maximum_temperature_reading = []
        minimum_temperature_reading = []
        mean_humidity_reading = []
        file_contents = file.readline()
        for iterator in range(1, size_of_the_file):
            file_contents = file.readline()
            make_reading = file_contents.split(',')
            maximum_temperature_reading.append(make_reading[1])
            minimum_temperature_reading.append(make_reading[3])
            mean_humidity_reading.append(make_reading[9])
            date_reading.append(make_reading[0])
    if calculate == '-a':
        calculate_average(maximum_temperature_reading, minimum_temperature_reading,
                          mean_humidity_reading)
    elif calculate == '-c':
        display_bar_charts(maximum_temperature_reading, minimum_temperature_reading)


def calculate_average(maximum_reading, minimum_reading, mean_reading):
    maximum_average_temperature = average_temp(maximum_reading)
    minimum_average_temperature = average_temp(minimum_reading)
    humidity_average = average_temp(mean_reading)
    display_average_temperatures(maximum_average_temperature,
                                 minimum_average_temperature, humidity_average)


def display_bar_charts(temperature_reading1, temperature_reading2):
    bar_charts(temperature_reading1, temperature_reading2)
    horizontal_bar_charts_weather(temperature_reading1, temperature_reading2)


def average_temp(temperature_reading):
    total = 0
    count = 0
    for iterator in range(0, len(temperature_reading)):
        if temperature_reading[iterator] != '':
            total = total + float(temperature_reading[iterator])
            count += 1
    return total / count


def display_average_temperatures(maxiM_average, minM_average, humidity_average):
    print(f'Average Highest Temperature : {maxiM_average}C')
    print(f'Average Lowest Temperature : {minM_average}C')
    print(f'Average Humidity : {humidity_average}%')


def bar_charts(temperature_reading_maximum, temperature_reading_minimum):
    Red = "\033[31m"
    Blue = "\033[34m"
    for iterator in range(0, len(temperature_reading_minimum)):
        if temperature_reading_maximum[iterator] == '':
            print('', end='')
        else:
            White = "\033[37m"
            print(White, iterator + 1, end='')
            display_blue_barchart(float(temperature_reading_maximum[iterator]), Red)
            print(White, int(temperature_reading_maximum[iterator]), end='')
            print('')
            print(White, iterator + 1, end='')
            display_blue_barchart(float(temperature_reading_minimum[iterator]), Blue)
            print(White, f'{int(temperature_reading_minimum[iterator])}C', end='')
            print('')


def horizontal_bar_charts_weather(temperature_reading_maximum, temperature_reading_minimum):
    Red = "\033[31m"
    Blue = "\033[34m"
    for iterator in range(0, len(temperature_reading_minimum)-1):
        if temperature_reading_maximum[iterator] == '':
            print('', end='')
        else:
            White = "\033[37m"
            print(iterator+1, end='')
            display_blue_barchart(float(temperature_reading_maximum[iterator]), Red)
            display_blue_barchart(float(temperature_reading_minimum[iterator]), Blue)
            print(White, f'{int(temperature_reading_maximum[iterator])}C-'
                  f'{int(temperature_reading_minimum[iterator])}C', end='')
            print('')


def display_blue_barchart(number, color):
    iterate = 1
    while iterate <= number:
        print(color + '+', end='')
        iterate += 1


# For year


def weather_man(year):
    files = os.listdir('.')
    file_reading = []
    for item in files:
        if year in item:  # given year or month
            file_reading.append(item)
    size = len(file_reading)
    making_year_temperature_readings(file_reading, size)


def making_year_temperature_readings(file_readings, number_of_the_files):
    maximum_temperatures = []
    minimum_temperatures = []
    minimum_temperature_dates = []
    maximum_temperature_dates = []
    mean_humidity = []
    mean_humidity_dates = []                 # I need these variables in and after the for loop
    for iterator in range(0, number_of_the_files):
        max_temperature_reading, min_temperature_reading, mean_humidity_reading, date_reading = \
         make_temperature_readings(file_readings[iterator])     # 1st function
        # we are calculating max month temp of every month in every iteration
        index_max = calculate_maximum_temperature(max_temperature_reading)
        maximum_temperature = max_temperature_reading[index_max]
        maximum_temperatures.append(maximum_temperature)
        maximum_temperature_dates.append(calculate_date(date_reading, index_max))

        # minimum
        index_min = calculate_minimum_temperature(min_temperature_reading)
        minimum_temperature = min_temperature_reading[index_min]
        minimum_temperatures.append(minimum_temperature)
        minimum_temperature_dates.append(calculate_date(date_reading, index_min))
        # humidity
        index_mean = calculate_maximum_temperature(mean_humidity_reading)
        mean_humidity1 = mean_humidity_reading[index_max]
        mean_humidity.append(mean_humidity1)
        mean_humidity_dates.append(calculate_date(date_reading, index_mean))

    display_results(maximum_temperatures, maximum_temperature_dates,
                    minimum_temperatures, minimum_temperature_dates,
                    mean_humidity, mean_humidity_dates)             # 2nd function

# 1st function


def calculate_date(date_reading, index):
    return date_reading[index]


def make_temperature_readings(file_name):
    with open(file_name, 'r') as file:
        size_of_the_file = file_size(file_name)
        date_reading = []
        max_temperature_reading = []
        min_temperature_reading = []
        mean_humidity_reading = []
        file_contents = file.readline()
        for iterator in range(1, size_of_the_file):
            file_contents = file.readline()
            reading_file = file_contents.split(',')
            max_temperature_reading.append(reading_file[1])
            min_temperature_reading.append(reading_file[3])
            mean_humidity_reading.append(reading_file[9])
            date_reading.append(reading_file[0])
    return max_temperature_reading, min_temperature_reading, mean_humidity_reading, date_reading


def file_size(file_name):
    file = open(file_name, "r")
    counter = 0
    # Reading from file
    Content = file.read()
    line_reading = Content.split("\n")
    for iterator in line_reading:
        if iterator:
            counter += 1
    return counter


# 2nd function

def display_results(maximum_reading, date_reading_max,
                    minimum_reading, date_reading_min,
                    humidity_reading, date_reading_humidity):

    index_maximum_temperature = calculate_maximum_temperature(maximum_reading)
    index_minimum_temperature = calculate_minimum_temperature(minimum_reading)
    index_maximum_humidity = calculate_maximum_temperature(humidity_reading)
    print(f'Max temperature is {maximum_reading[index_maximum_temperature]}C on '
          f'{date_reading_max[index_maximum_temperature]}')
    print(f'Min temperature is {minimum_reading[index_minimum_temperature]}C on '
          f'{date_reading_min[index_minimum_temperature]}')
    print(f'Max Humidity is {humidity_reading[index_maximum_humidity]}% on '
          f'{date_reading_humidity[index_maximum_humidity]}')


def calculate_maximum_temperature(temperature_readings):
    maximum1 = 0
    for iterator in range(0, len(temperature_readings)):
        if temperature_readings[iterator] != '':
            if float(temperature_readings[iterator]) >= maximum1:
                maximum1 = float(temperature_readings[iterator])
                maximum2 = iterator
            else:
                temperature_readings[iterator] = temperature_readings[iterator]
    return maximum2


def calculate_minimum_temperature(temperature_readings):
    minimum1 = float(temperature_readings[0])
    minimum2 = 0
    for iterator in range(1, len(temperature_readings)):
        if temperature_readings[iterator] != '':
            if float(temperature_readings[iterator]) < minimum1:
                minimum1 = float(temperature_readings[iterator])
                minimum2 = iterator
            else:
                minimum1 = minimum1
    return minimum2


# Main

if __name__ == '__main__':

    months = ['Jan', 'Feb', 'Mar',
              'April', 'May', 'Jun',
              'Jul', 'Aug', 'Sep',
              'Oct', 'Nov', 'Dec']
    if len(sys.argv) == 3:
        name = sys.argv[1].split('/')
        name.append(sys.argv[2])
        if len(name) == 3 and sys.argv[2] == '-c' or sys.argv[2] == '-a':
            weather_month(name[0], months[int(name[1])-1], name[2])
        elif len(name) == 2 and name[1] == '-e':
            weather_man(name[0])
        else:
            print('Wrong Input')
    else:
        print('Wrong Input')

