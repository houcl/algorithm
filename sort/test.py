# -*- coding: utf-8 -*-

#冒泡排序
def bubble_sort(list_data, sort=False):
    re_list = []

    length_list = len(list_data)
    while length_list > 0:
        for i in range(length_list-1):
            if sort:
                if list_data[i] > list_data[i+1]:
                    a = list_data[i+1]
                    list_data[i + 1] = list_data[i]
                    list_data[i] = a
            else: #加入倒序逻辑
                if list_data[i] < list_data[i+1]:
                    a = list_data[i+1]
                    list_data[i + 1] = list_data[i]
                    list_data[i] = a

        re_list.append(list_data[length_list-1])
        length_list -= 1
    return re_list

def quick_sort_v2(data_list):
    if not data_list:
        return data_list

    bigList = []
    smallList = []
    minddle = data_list[0]
    for i in data_list[1:]:
        if i < minddle:
            smallList.append(i)
        else:
            bigList.append(i)

    return quick_sort_v2(smallList) + [minddle] + quick_sort_v2(bigList)

if __name__ == '__main__':
    list_d = [6,7,8,4,2,3]
    print(quick_sort_v2(list_d))
    #print(quick_sort(list_d, 0, len(list_d)-1))

    #print(bubble_sort(list_d))