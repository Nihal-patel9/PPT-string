def reconstruct_permutation(s):
    perm = []
    start = 0
    end = len(s)

    for ch in s:
        if ch == 'I':
            perm.append(start)
            start += 1
        elif ch == 'D':
            perm.append(end)
            end -= 1

    perm.append(start)

    return perm


s = "IDID"
perm = reconstruct_permutation(s)
print(perm)
