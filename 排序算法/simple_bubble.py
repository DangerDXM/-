"""
简单的冒泡排序:
每一个关键字都和后面的关键字进行比较，如果大则交换。

缺陷：只能定一个数字的位置，一次排序对其他数字没有好处。
"""

if __name__ == '__main__':
    lis = [9, 1, 5, 8, 3, 7, 4, 6, 2]
    print('原始数组：{}'.format(lis))
    for i in range(len(lis)):
        for j in range(i+1, len(lis)):
            if lis[i] > lis[j]:
                lis[i], lis[j] = lis[j], lis[i]
    print('排序后的数组：{}'.format(lis))
