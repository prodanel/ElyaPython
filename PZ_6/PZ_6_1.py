def is_arithmetic_progression(arr):
    if len(arr) < 2:
        return 0
    arr.sort()
    common_difference = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if arr[i] - arr[i - 1] != common_difference:
            return 0
    return common_difference
N = [3, 1, 5, 7]
result = is_arithmetic_progression(N)
print(result)
