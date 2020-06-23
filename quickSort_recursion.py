# 递归版本的快速排序
import random


def partition(data, length, start, end):
    if not data or length <= 0 or start < 0 or end >= length:
        raise ValueError

    index = random.randint(start, end)
    data[index], data[end] = data[end], data[index]

    small = start - 1
    for index in range(start, end):
        if data[index] < data[end]:
            small += 1
            if small != index:
                data[small], data[index] = data[index], data[small]
    small += 1
    data[small], data[end] = data[end], data[small]

    return small


def quickSort(data, length, start, end):
    if start == end:
        return
    index = partition(data, length, start, end)
    if index > start:
        quickSort(data, length, start, index - 1)
    if index < end:
        quickSort(data, length, index + 1, end)


def main():
    data = [3, 7, 9, 1, 4, 8, 10, 6, 2]
    print('排序前数组：', data)
    print('=========================================')
    start = 0
    length = len(data)
    end = length - 1
    quickSort(data, length, start, end)
    print('排序后数组：', data)


if __name__ == '__main__':
    main()
