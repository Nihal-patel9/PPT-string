def findMaxLength(nums):
    max_length = 0
    count = 0
    sum_counts = {0: -1}

    for i, num in enumerate(nums):
        count += 1 if num == 1 else -1

        if count in sum_counts:
            length = i - sum_counts[count]
            max_length = max(max_length, length)
        else:
            sum_counts[count] = i

    return max_length


nums = [0, 1]
print(findMaxLength(nums))  # Output: 2
