x=int(input("Enter Your Marks:"))

if 100>=x>=0:
    if 100>=x>=80:
        print("A+")
    elif 80>x>=70:
        print("A")
    elif 70>x>=60:
        print("A-")
    elif 60>x>=50:
        print("B")
    elif 50>x>=40:
        print("C")
    elif 40>x>=33:
        print("D")
    else:
        print("Fail")
else:
    print("Your Entered Marks",x,"is Wrong. Please Enter Valid Marks.")