name=input("Podaj imie")
print("typ",type(name))

number=int(input("podaj liczbe"))
print("typ", type(number))

print(4/9)
print(25/5)

print(4+5)
print(9/3)
print(3-1)

a=5
a+=1
print(a)
a**=2
print(a)

a=3
a+=2
print(a)
a**=3
print(a)

a=True
b=False
print(a or b)
print(type(a))

a=5
b=a
b+=(a)
print(b)

a=5
if a >0:
    print("liczba dodatnia")
elif a==0:
    print("zero")
else:
    print("liczba ujemna")

a=0
if a >=0:
    print("liczba dodatnia")
elif a==0:
    print("zero")
else:
    print("liczba ujemna")
