N = int(input("Введите число N (>0): "))
K = 0
while (K + 1) ** 2 < N:
    K += 1
print(f"Наибольшее целое число K, квадрат которого не превосходит N: {K}")
