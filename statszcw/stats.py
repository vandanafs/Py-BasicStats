import math
from typing import List
from typing import List
import numpy as np
import future as future


def zcount(list: List[float]) ->float:
     return len(list)

def zmean(list: List[float]) ->float:
    return sum(list)/len(list)


def zmode(list: List[float]) -> float : #max occureence
    #using iterable it count the max occureence from org list
    # return max(set(list),key=list.count)
    count_element={}
    for element in list:
        try:
          count_element[element]+=1   # adding actual count of that element to value of dict
        except:
          count_element[element]=0

    #print(count_element)
   # print(list)

    mode=0
    for count in count_element:
        if count >mode:
           mode=count
    return mode

def zmedian(list: List[float]) -> float:
    # asending with middle number 
    total = len(list)
    for i in range(total):
        for j in range(i + 1, total):
            if (list[i] > list[j]):
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    print(f'Asending list :{list}')
    mid = (total // 2)
    if total % 2 != 0:
        print(f'Mid Element at index {mid}')
        print(f'Mid value when list size is odd {list[mid]}')
    else:
        print(mid - 1, mid)
        sum = list[mid - 1] + list[mid]
        avg = sum / 2
        #print(f'Mean of 2 values{avg}')
    return avg

def zvariance(list: List[float]) -> float :

    n = zcount(list) - 1
    mean = zmean(list)
    dev = [abs(mean-xi)**2 for xi in list]  # list comprehensive
    variance = sum(dev)/n
    return variance


def zstddev(list: List[float]) -> float:
    return math.sqrt(zvariance(list))


def zstderr(list: List[float]) -> float:
    return zstddev(list)/math.sqrt(zcount(list))



def zcorr1(listx: List[float], listy: List[float]) -> float:
    sum = 0

    sub_x = [i - zmean(listx) for i in listx]
    sub_y = [i - zmean(listy) for i in listy]
    lengthx = zcount(listx)
    lengthy = zcount(listy)

    num_list = [sub_x[i] * sub_y[i] for i in range(lengthx)] # multiple x*y
    #print(num_list)
    num = 0
    for i in num_list:
        #print(i)
        num = num + i  # sum of multiplid list
    den = lengthx - 1
    cov = num / den

    if lengthx == lengthy:
        return cov / (zstddev(listx) * zstddev(listy))

    else:
        return cov

    def zcorr(listx: List[float], listy: List[float]) -> float:
        # sum(xy) ,sum(x), sum(y)
        x_multiply_y = np.multiply(listx, listy)  # multiplied list
        sum_xy = sum(x_multiply_y)
        print(f'sum of xy {sum_xy}')
        sum_x = sum(listx)
        sum_y = sum(listy)
        lengthx = zcount(listx)
        lengthy = zcount(listy)
        if lengthx == lengthy:
            co_relation = ((lengthx * sum_xy) - sum_x * sum_y) / (zstddev(listx) * zstddev(listy))
        return co_relation


def read_data_file(file_name):
    x,y = [], []
    with open(file_name) as f:
        f_line =f.readline()  # discord header from csv file
        for line in f :
            row=line.split(',')
            x.append(float(row[0]))
            y.append(float(row[1]))
    return(x,y)

def read_data_sets(files):  # more than one file
    data= {}
    for file in files:
        data[file]=read_data_file(file)
    return data


if __name__=='__main__':
    list1=[43,21,25,42,57,59]
    list2=[99,65,79,75,87,81]
    print(zcount(list1))
   # print(zmode(list))
   # print(zmedian(list1))
    #list = [1, 2, 3, 4, 5]
    print(zvariance(list1))
    print(f'list 1 std devi  {zstddev(list1)}')
    print(f'list 2 std devi  {zstddev(list2)}')
    print( zstderr(list1))
    print(zcorr1(list1, list2))
    print(f'Formula for corelation{zcorr(list1, list2)}')