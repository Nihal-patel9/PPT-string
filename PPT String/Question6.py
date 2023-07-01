from collections import defaultdict


def findOriginalArray(changed):
    count = defaultdict(int)
    for num in changed:
        count[num] += 1

    original = []
    for num in sorted(changed):
        if count[num] > 0 and count[num // 2] > 0:
            count[num] -= 1
            count[num // 2] -= 1
            original.append(num // 2)

    if len(original) == len(changed) // 2:
        return original
    else:
        return []


changed = [1, 3, 4, 2, 6, 8]
print(findOriginalArray(changed))  # Output: [1, 3, 4]
