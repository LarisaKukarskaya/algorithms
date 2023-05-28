n = input()
arr = [int(i) for i in input().split()]
k = int(input())


def twosum_with_sort(numbers, X):
    numbers.sort()

    left = 0
    right = len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == X:
            return f'{numbers[left]} {numbers[right]}'
        elif current_sum < X:
            left += 1
        else:
            right -= 1


print(twosum_with_sort(arr, k))
