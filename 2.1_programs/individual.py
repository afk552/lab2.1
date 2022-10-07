import math

a = int(input("Type upper side of trapezoid: "))
b = int(input("Type bottom side of trapezoid: "))
h = int(input("Enter height of trapezoid: "))

n = abs(a - b) / 2  # вычисляем нижний катет
c = math.sqrt((n ** 2) + (h ** 2))  # вычисляем гипотенузу
P = 2 * c + a + b  # вычисляем периметр

print("Perimeter is: %.3f" % (P))
