i = int(input("Enter your marks: "))

if i > 100:
    print("Opps! It's a wrong marks \n Please Enter Valid Marks")
elif i >= 80:
    print("A+")
elif i >= 70:
    print("A")
elif i >= 60:
    print("A-")
elif i >= 50:
    print("B")
elif i >= 40:
    print("C")
elif i >= 33:
    print("D")
elif i >= 0:
    print("Fail")
else:
    print("Opps! It's a wrong marks \n Please Enter Valid Marks")
