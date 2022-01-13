import os
import sys


def make_temperature_lists(file_name):
    with open(file_name, 'r') as f:
        min_temperature = 0
        file_size = reading_file(file_name)
        date_list = []
        max_temperature_list = []
        make_list = []
        min_temperature_list = []
        mean_list_humidity = []
        file_contents = []
        file_contents = f.readline()
        i = 1
        while i < file_size:
            file_contents = f.readline()
            make_list = file_contents.split(',')
            max_temperature_list.append(make_list[1])
            min_temperature_list.append(make_list[3])
            mean_list_humidity.append(make_list[9])
            date_list.append(make_list[0])
            i += 1
    return max_temperature_list, min_temperature_list, mean_list_humidity, date_list


def reading_file(file_name):
    file = open(file_name, "r")
    Counter = 0
    # Reading from file
    Content = file.read()
    CoList = Content.split("\n")
    for i in CoList:
        if i:
            Counter += 1
    return Counter


def maximum_temp(l1):
    maxi = 0
    maxi2 = 0
    i = 0
    while i < len(l1):
        if l1[i] != '':
            if float(l1[i]) >= maxi:
                maxi = float(l1[i])
                maxi2 = i
            else:
                l1[i] = l1[i]
        i += 1
    return maxi2


def temp_date(l1, index):
    return l1[index]


def minimum_temp(l1):
    min1 = float(l1[0])
    min2 = 0
    j = 1
    while j < len(l1):
        if l1[j] != '':
            if float(l1[j]) < min1:
                min1 = float(l1[j])
                min2 = j
            else:
                min1 = min1
        j += 1
    return min2


def make_month_lists(file_name):
    with open(file_name, 'r') as f:
        file_size = reading_file(file_name)
        dateM_list = []
        maxiM_temperature_list = []
        make_tlist = []
        miniM_temperature_list = []
        meanH_list_humidity = []
        file_contents = []
        file_contents = f.readline()
        i = 1
        while i < file_size:
            file_contents = f.readline()
            make_tlist = file_contents.split(',')
            maxiM_temperature_list.append(make_tlist[1])
            miniM_temperature_list.append(make_tlist[3])
            meanH_list_humidity.append(make_tlist[9])
            dateM_list.append(make_tlist[0])
            i += 1
        maxiM_average = average_temp(maxiM_temperature_list)
        minM_average = average_temp(miniM_temperature_list)
        humidity_average = average_temp(meanH_list_humidity)
        print(f'Average Highest Temperature : {maxiM_average}C')
        print(f'Average Lowest Temperature : {minM_average}C')
        print(f'Average Humidity : {humidity_average}%')
        bar_charts(maxiM_temperature_list, miniM_temperature_list)
        horizontal_bar_charts(maxiM_temperature_list, miniM_temperature_list)


def average_temp(l1):
    sum1 = 0
    count = 0
    i = 0
    while i < len(l1):
        if l1[i] != '':
            sum1 = sum1 + float(l1[i])
            count += 1
        i += 1
    return sum1 / count


def horizontal_bar_charts(l1, l2):
    temp1 = 0
    Red = "\033[31m"
    Blue = "\033[34m"
    White = "\033[37m"
    print(White + 'The Horizontal Bar charts for temperatures are :')
    while temp1 < len(l2):
        if l2[temp1] == '':
            print('', end='')
        else:
            temp2 = 0
            temp3 = 0
            temp4 = 0
            print(temp1 + 1, end='')
            while temp2 < float(l2[temp1]):
                print(Blue + '+', end='')
                temp2 += 1
            while temp3 <= temp1:
                if l1[temp1] == '':
                    print('', end='')
                else:
                    while temp4 < float(l1[temp1]):
                        print(Red + '+', end='')
                        temp4 += 1
                temp3 += 1
            print('')
        temp1 += 1
    print('')


def bar_charts(l1, l2):
    k = 0
    Red = "\033[31m"
    Blue = "\033[34m"
    print('The bar chart for temperatures are :')
    while k < len(l1):
        if l1[k] == '':
            print('', end='')
        else:
            t = 0
            m = 0
            n = 0
            while t < float(l1[k]):
                print(Red + '+', end='')
                t += 1
            print('')
            while m <= t:
                if l2[t] == '':
                    print('', end='')
                else:
                    while n < float(l2[t]):
                        print(Blue + '+', end='')
                        n += 1
                m += 1
            print('')
        k += 1
    print('')


def make_results(l1, d1, l2, d2, l3, d3):
    max1 = maximum_temp(l1)
    min1 = minimum_temp(l2)
    meanH = maximum_temp(l3)
    print(f'Max temperature is {l1[max1]}C on {d1[max1]}')
    print(f'Min temperature is {l2[min1]}C on {d2[min1]}')
    print(f'Max Humidity is {l3[meanH]}C on {d3[meanH]}')


def make_list(l1, list_size):
    max_temp = []
    min_temp = []
    min_date = []
    max_date = []
    mean_humidity = []
    mean_date = []
    index_max = 0
    index_min = 0
    index_mean = 0
    k = 0
    while k < list_size:
        max_temperature_list, min_temperature_list, mean_temperature_list, date_list = \
            make_temperature_lists(l1[k])
        # we have list for every month in every iteration
        index_max = maximum_temp(max_temperature_list)
        max_temp1 = max_temperature_list[index_max]
        max_temp.append(max_temp1)
        max_date.append(temp_date(date_list, index_max))

        # minimum
        index_min = minimum_temp(min_temperature_list)
        min_temp1 = min_temperature_list[index_min]
        min_temp.append(min_temp1)
        min_date.append(temp_date(date_list, index_min))
        # humidity
        index_mean = maximum_temp(mean_temperature_list)
        mean_temp1 = mean_temperature_list[index_max]
        mean_humidity.append(mean_temp1)
        mean_date.append(temp_date(date_list, index_mean))

        k += 1
    make_results(max_temp, max_date, min_temp, min_date, mean_humidity, mean_date)


def weatherMan(year):
    arr = os.listdir('.')
    file_lists = []
    for item in arr:
        if year in item:  # given year or month
            file_lists.append(item)
    size = len(file_lists)
    make_list(file_lists, size)


def weatherMonth(year, month):
    fName = ''
    arr = os.listdir('.')
    file_lists = []
    for item in arr:
        if year in item and month in item:  # given year or month
            fName = item
    make_month_lists(fName)


#
print(len(sys.argv))
if len(sys.argv) == 1:
    print('Month or year were not provided')
elif len(sys.argv) == 2:
    weatherMan(sys.argv[1])
elif len(sys.argv) == 3:
    weatherMonth(sys.argv[1], sys.argv[2])
else:
    print('Wrong Input')
