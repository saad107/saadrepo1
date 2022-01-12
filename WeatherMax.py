def tempLists(filName):
    with open(filName, 'r') as f:
        minT = 0
        dateList = []
        maxList2 = []
        bList = []
        minList3 = []
        meanHumList = []
        mContents = []
        mContents = f.readline()
        i = 1
        while i <= 31:
            mContents = f.readline()
            bList = mContents.split(',')
            maxList2.append(bList[1])
            minList3.append(bList[3])
            meanHumList.append(bList[9])
            dateList.append(bList[0])
            i += 1
        minT = minTemp(minList3)
        maxTemp1 = maxTemp(maxList2)
        print(f'Max temp for the month is : {maxList2[maxTemp1]}C on the date {date(dateList, maxTemp1)}')
        print(f'Min temp for the month is : {minList3[minT]}C on the date {date(dateList, minT)}')
        print(f'Max Average temp is {avgTemp(maxList2)}C ')
        print(f'Min Average temp is {avgTemp(minList3)}C ')
        print(f'Max Mean Humidity is {avgTemp(meanHumList)}% ')
        maxBarChart(maxList2, minList3)
        maxBarChartHorizontal(maxList2, minList3)


def maxBarChartHorizontal(l1, l2):
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


def maxBarChart(l1, l2):
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


def date(l1, indx):
    return l1[indx]


def avgTemp(l1):
    sum1 = 0
    count = 0
    i = 0
    while i < len(l1):
        if l1[i] != '':
            sum1 = sum1 + float(l1[i])
            count += 1
        i += 1
    return sum1 / count


def maxTemp(l1):
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


def minTemp(l1):
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


def readfile(name):
    fContents = []
    with open(name, 'r') as f:
        fContents = f.readlines()
        return fContents


# main


name = input("Enter the month (Jan/Aug/Dec/Mar) ")
year = input("Enter the year (2004/2008) ")
fName = f'Murree_weather_{year}_{name}.txt'
readfile(fName)
tempLists(fName)
