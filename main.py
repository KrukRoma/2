#1
a = int(input("Введіть перше число : "))
b = int(input("Введіть друге число : "))
c = int(input("Введіть третє число : "))
sum = a + b + c
dob = a * b * c
print(sum)
print(dob)

#2
d = int(input("Введіть перше число : "))
e = int(input("Введіть друге число : "))
f = int(input("Введіть третє число : "))
if d>e>f:
    print(d)
if d>f>e:
    print(d)
if e>d>f:
    print(e)
if e>f>d:
    print(e)
if f>e>d:
    print(f)
if f>d>e:
    print(f)
x = (d + e + f)//3
print(x)

#3
m = int(input("Введіть кількість метрів : "))
ml = m * 0.00062137
print(f"{ml} миль")
dm = m * 39.37
print(f"{dm} дюймів")
yard = m * 1.0936
print(f"{yard} ярдів")