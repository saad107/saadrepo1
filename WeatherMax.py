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
        min_temperature = minimum_temp(min_temperature_list)
        max_temperature = maximum_temp(max_temperature_list)
        print(f'Max temp for the month is : {max_temperature_list[max_temperature]}C on the date '
              f'{temp_date(date_list, max_temperature)}')
        print(f'Min temp for the month is : {min_temperature_list[min_temperature]}C on the date '
              f'{temp_date(date_list, min_temperature)}')
        print(f'Max Average temp is {average_temp(max_temperature_list)}C ')
        print(f'Min Average temp is {average_temp(min_temperature_list)}C ')
        print(f'Max Mean Humidity is {average_temp(mean_list_humidity)}% ')
        bar_charts(max_temperature_list, min_temperature_list)
        horizontal_bar_charts(max_temperature_list, min_temperature_list)


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
            print(temp1+1, end='')
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


def temp_date(l1, index):
    return l1[index]


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


def maximum_temp(l1):
    maxi = ''
    maxi2 = 0
    i = 0
    while i < len(l1):
        if l1[i] >= maxi:
            maxi = l1[i]
            maxi2 = i
        else:
            l1[i] = l1[i]
        i += 1
    return maxi2


def minimum_temp(l1):
    min1 = l1[0]
    min2 = 0
    j = 1
    while j < len(l1):
        if l1[j] != '':
            if l1[j] < min1:
                min1 = l1[j]
                min2 = j
            else:
                min1 = min1
        j += 1
    return min2

# main
# Provide month and year it will calculate the minimum,Maximum average Max temperature Average Min temperature
# and bar charts horizontal and simple bar charts


month_name = input("Enter the month (Jan/Aug/Dec/Mar) ")
year = input("Enter the year (2004/2008) ")
file_Name = f'Murree_weather_{year}_{month_name}.txt'
reading_file(file_Name)
make_temperature_lists(file_Name)

