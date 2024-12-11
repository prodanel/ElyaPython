def closest_point(A):
    closest = None
    min_distance = float('inf')
    for (x, y) in A:
        if (x > 0 and y > 0) or (x < 0 and y < 0):
            distance = (x**2 + y**2)**0.5
            if distance < min_distance:
                min_distance = distance
                closest = (x, y)
    return closest if closest is not None else (0, 0)
A = [(1, 2), (-3, -4), (2, 3), (-1, -1)]
result = closest_point(A)
print(result)
