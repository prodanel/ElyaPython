import math
def TrianglePS(a):
    P = 3 * a
    S = (a ** 2 * math.sqrt(3)) / 4
    return P, S
sides = [3, 5, 7]
for side in sides:
    perimeter, area = TrianglePS(side)
    print(f"Треугольник со стороной {side}: Периметр = {perimeter}, Площадь = {area:.2f}")
