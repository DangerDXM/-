"""
正宗的冒泡排序：每一趟排序，先定位数组未排序的其实位置。然后从后向前遍历，
    不断将小的数字提前，这样不仅可以一趟找到最小的数字，也能让其他数字接近
    自己应该在的位置。
优化：如果一趟排序下来，没有发生交换操作，则数组已经拍好序。
"""


if __name__ == '__main__':
    lis = [1, 2, 3, 4, 5, 6, 7, 9, 8]   # [9, 1, 5, 8, 3, 4, 6, 2]
    print("原始数组：", lis)

    # flag 为标志，如果一趟排序没有发生交换，则数组已经有序。
    flag = True

    for i in range(len(lis)):
        if not flag:
            break
        print("第%d趟排序..." % (i+1))  # 记录数组排序的次数

        for j in range(len(lis)-2, i-1, -1):
            if lis[j] > lis[j+1]:
                lis[j], lis[j+1] = lis[j+1], lis[j]
            else:
                flag = not flag
    print("================排序结束===============\n")
    print("排序后数组：", lis)
