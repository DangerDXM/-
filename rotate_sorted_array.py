def main():
    numbers = [2, 2, 2, 0, 1]
    if not numbers:
        print(-1)

    low = 0
    high = len(numbers) - 1
    mid = low

    while numbers[low] >= numbers[high]:
        if high - low == 1:
            mid = high
            break

        mid = int((low + high) / 2)
        if numbers[low] == numbers[high] and numbers[low] == numbers[mid]:
            result = seqQuerry(low, high, numbers)
            print(result)
            break

        if numbers[low] <= numbers[mid]:
            low = mid
        elif numbers[high] >= numbers[mid]:
            high = mid
    print(numbers[mid])


def seqQuerry(start, end, numbers):
    min_num = numbers[start]
    for i in range(start, end + 1):
        if min_num > numbers[i]:
            min_num = numbers[i]
    return min_num


if __name__ == '__main__':
    main()
