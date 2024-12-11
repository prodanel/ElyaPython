def transform_list(A):
    B = []
    for AK in A:
        if AK < 5:
            B.append(2 * AK)
        else:
            B.append(AK / 2)
    return B
A = [1, 9, 3, 6, 8]
B = transform_list(A)
print(B)
