import os
import sys


def weatherMonth(year, month, res):
    file_name = ''
    arr = os.listdir('.')
    for item in arr:
        if year in item and month in item:  # given year or month
            file_name = item
    make_month_lists(file_name, res)


def make_month_lists(file_name, res):
    with open(file_name, 'r') as file:
        size_of_the_file = file_size(file_name)
        dateM_list = []
        maximum_temperature_reading = []
        minimum_temperature_reading = []
        mean_humidity_reading = []
        file_contents = file.readline()
        i = 1
        while i < size_of_the_file:
            file_contents = file.readline()
            make_tlist = file_contents.split(',')
            maximum_temperature_reading.append(make_tlist[1])
            minimum_temperature_reading.append(make_tlist[3])
            mean_humidity_reading.append(make_tlist[9])
            dateM_list.append(make_tlist[0])
            i += 1
    if res == '-a':
        calculate_average(maximum_temperature_reading, minimum_temperature_reading, mean_humidity_reading)
    elif res == '-c':
        display_bar_charts(maximum_temperature_reading,minimum_temperature_reading)


def calculate_average(l1, l2, l3):
    maximum_average_temperature = average_temp(l1)
    minimum_average_temperature = average_temp(l2)
    humidity_average = average_temp(l3)
    display_average_temperatures(maximum_average_temperature, minimum_average_temperature, humidity_average)


def display_bar_charts(temperature_reading1,temperature_reading2):
    bar_charts(temperature_reading1, temperature_reading2)
    horizontal_bar_charts_weather(temperature_reading1, temperature_reading2)


def average_temp(temperature_reading):
    sum1 = 0
    count = 0
    iterator = 0
    while iterator < len(temperature_reading):
        if temperature_reading[iterator] != '':
            sum1 = sum1 + float(temperature_reading[iterator])
            count += 1
        iterator += 1
    return sum1 / count


def display_average_temperatures(maxiM_average, minM_average, humidity_average):
    print(f'Average Highest Temperature : {maxiM_average}C')
    print(f'Average Lowest Temperature : {minM_average}C')
    print(f'Average Humidity : {humidity_average}%')


def bar_charts(l1, l2):
    iterator = 0
    Red = "\033[31m"
    Blue = "\033[34m"
    while iterator < len(l2):
        if l1[iterator] == '':
            print('', end='')
        else:
            White = "\033[37m"
            print(White, iterator + 1, end='')
            display_blue_barchart(float(l1[iterator]), Red)
            print('')
            print(White,iterator + 1, end='')
            display_blue_barchart(float(l2[iterator]), Blue)
            print('')
        iterator += 1


def horizontal_bar_charts_weather(l1, l2):
    iterator = 0
    Red = "\033[31m"
    Blue = "\033[34m"
    while iterator < len(l2):
        if l1[iterator] =='':
            print('', end='')
        else:
            print(iterator+1, end='')
            display_blue_barchart(float(l1[iterator]), Red)
            display_blue_barchart(float(l1[iterator]), Blue)
            print('')
        iterator += 1


def display_blue_barchart(number, color):
    iterate = 1

    while iterate <= number:
        print(color + '+', end='')
        iterate += 1

# For year


def weatherMan(year):
    arr = os.listdir('.')
    file_lists = []
    for item in arr:
        if year in item:  # given year or month
            file_lists.append(item)
    size = len(file_lists)
    making_year_temperature_readings(file_lists, size)


def making_year_temperature_readings(l1, number_of_the_files):
    max_temp = []
    min_temp = []
    min_date = []
    max_date = []
    mean_humidity = []
    mean_date = []
    iterator = 0
    while iterator < number_of_the_files:
        max_temperature_reading, min_temperature_reading, mean_humidity_reading, date_reading = \
            make_temperature_readings(l1[iterator])     # 1st function
        # we are calculating max month temp of every month in every iteration
        index_max = calculate_maximum_temperature(max_temperature_reading)
        max_temp1 = max_temperature_reading[index_max]
        max_temp.append(max_temp1)
        max_date.append(temp_date(date_reading, index_max))

        # minimum
        index_min = calculate_minimum_temperature(min_temperature_reading)
        min_temp1 = min_temperature_reading[index_min]
        min_temp.append(min_temp1)
        min_date.append(temp_date(date_reading, index_min))
        # humidity
        index_mean = calculate_maximum_temperature(mean_humidity_reading)
        mean_temp1 = mean_humidity_reading[index_max]
        mean_humidity.append(mean_temp1)
        mean_date.append(temp_date(date_reading, index_mean))

        iterator += 1
    make_results(max_temp, max_date, min_temp, min_date, mean_humidity, mean_date)  # 2nd function

# 1st function


def temp_date(l1, index):
    return l1[index]


def make_temperature_readings(file_name):
    with open(file_name, 'r') as file:
        min_temperature = 0
        size_of_the_file = file_size(file_name)
        date_reading = []
        max_temperature_reading = []
        min_temperature_reading = []
        mean_humidity_reading = []
        file_contents = file.readline()
        iterator = 1
        while iterator < size_of_the_file:
            file_contents = file.readline()
            reading_file = file_contents.split(',')
            max_temperature_reading.append(reading_file[1])
            min_temperature_reading.append(reading_file[3])
            mean_humidity_reading.append(reading_file[9])
            date_reading.append(reading_file[0])
            iterator += 1
    return max_temperature_reading, min_temperature_reading, mean_humidity_reading, date_reading


def file_size(file_name):
    file = open(file_name, "r")
    counter = 0
    # Reading from file
    Content = file.read()
    co_list = Content.split("\n")
    for iterator in co_list:
        if iterator:
            counter += 1
    return counter


# 2nd function

def make_results(maximum_reading, date_reading_max, minimum_reading, date_reading_min,
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


def calculate_maximum_temperature(l1):
    maximum1 = 0
    iterator = 0
    while iterator < len(l1):
        if l1[iterator] != '':
            if float(l1[iterator]) >= maximum1:
                maximum1 = float(l1[iterator])
                maximum2 = iterator
            else:
                l1[iterator] = l1[iterator]
        iterator += 1
    return maximum2


def calculate_minimum_temperature(l1):
    min1 = float(l1[0])
    min2 = 0
    iterator = 1
    while iterator < len(l1):
        if l1[iterator] != '':
            if float(l1[iterator]) < min1:
                min1 = float(l1[iterator])
                min2 = iterator
            else:
                min1 = min1
        iterator += 1
    return min2


# Main


months = ['Jan', 'Feb', 'Mar', 'April', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
if len(sys.argv) == 3:
    name = sys.argv[1].split('/')
    name.append(sys.argv[2])
    if len(name) == 3:
        weatherMonth(name[0], months[int(name[1])-1], name[2])
    elif len(name) == 2:
        weatherMan(name[0])
