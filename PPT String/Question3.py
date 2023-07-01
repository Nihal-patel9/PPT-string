def validMountainArray(arr):
    n = len(arr)

    if n < 3:
        return False

    peak = -1

    for i in range(1, n - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            peak = i

    if peak == -1 or peak == 0 or peak == n - 1:
        return False

    for i in range(peak):
        if arr[i] >= arr[i + 1]:
            return False

    for i in range(peak, n - 1):
        if arr[i] <= arr[i + 1]:
            return False

    return True


arr = [2, 1]
print(validMountainArray(arr))  # Output: False
