num = int(input("Enter the number you want to check: "))
check = int(input("Enter the number divided by"))

if num%4 == 0:
    print("Number is multiple of 4")
elif num%2 == 2:
    print("Number is Even")
else:
    print("Number is odd")

if num%check == 0:
    print(num, "divides evenly by", check)
else:
    print(num,"does not divides evenly by",check)
    