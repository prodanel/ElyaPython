N = int(input("Введите число N: "))
K = int(input("Введите число K: "))
summa = 0
for i in range(1, N+1):
    summa += i ** K
print(f"Сумма 1^{K} + 2^{K} + ... + {N}^{K} равна {summa}")
