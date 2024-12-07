#Write a python program to find Maximum and Minimum Number.

a = int(input("Enter 1st Number :"))
b = int(input("Enter 2nd Number :"))
c = int(input("Enter 3rd Number :"))

if a > b and a > c :
    print(a,"is Greater")
elif b > a and b > c:
    print(b,"is Greater")
else:
    print(c,"is Greater")
#---------------------------------------------
if a < b and a < c :
    print(a,"is Lower")
elif b < a and b < c:
    print(b,"is Lower")
else:
    print(c,"is Lower")
#---------------------------------------------