def swape_item(goald_list, start_pointer, end_pointer):
    temp = goald_list[start_pointer]
    goald_list[start_pointer] = goald_list[end_pointer]
    goald_list[end_pointer] = temp

# !!!!


def insertion_sort(list_number):
    for i in range(len(list_number)):
        for j in range(i, 0, -1):
            if (list_number[j] < list_number[j-1]):
                swape_item(goald_list=list_number,
                           start_pointer=j, end_pointer=j-1)
            else:
                break
    return list_number

# !!!!


def bubble_sort(list_number):
    for i in range(len(list_number)):
        for j in range(len(list_number)-1):
            if (list_number[j] > list_number[j+1]):
                swape_item(goald_list=list_number,
                           start_pointer=j, end_pointer=j+1)
            else:
                continue
    return list_number

# !!!!


def selection_sort(list_number):
    for i in range(len(list_item)):
        min_item = min(list_item[i::])
        min_index = list_number[i::].index(min_item)+i
        swape_item(goald_list=list_number,
                   start_pointer=i, end_pointer=min_index)
    return list_number

# !!!!


def merge_sort(list_number):
    if (len(list_number) == 1):
        return list_number
    half_length_list = len(list_number)//2
    left_list = merge_sort(
        list_number=list_number[0:half_length_list])  # ? left side
    right_list = merge_sort(
        list_number=list_number[half_length_list:])  # ? right side
    return merge_two_list(left_list=left_list, right_list=right_list)


def merge_two_list(left_list, right_list):
    sort_list = []
    i = j = 0
    while i != len(left_list) and j != len(right_list):
        if (left_list[i] < right_list[j]):
            sort_list.append(left_list[i])
            i += 1
        else:
            sort_list.append(right_list[j])
            j += 1
    if (i < len(left_list)):
        sort_list += left_list[i::]
    if (j < len(right_list)):
        sort_list += right_list[j::]
    return sort_list

# !!!!


def bucket_sort(list_number):
    items = [[], [], []]
    for item in list_number:
        match len(str(item)):
            case 1:
                items[0].append(item)
            case 2:
                items[1].append(item)
            case 3:
                items[2].append(item)
    for i in range(len(items)):
        items[i] = bubble_sort(items[i])
    combines_items = []
    for i in items:
        combines_items.extend(i)
    return combines_items


list_item = [900, 9, 810, 7, 6, 5, 40, 2, 3, 4, 5, 84,
             74, 5, 689, 74, 5, 471, 200, 54, 1, 2, 545, 4, 56]
print(f'orginal list {list_item}')
sorted_list = bucket_sort(list_number=list_item)
print(f'sorted lis is {sorted_list}')
