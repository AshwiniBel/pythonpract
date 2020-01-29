marks = int(input("Enter the marks"))
if marks>= 75 and marks <=100:
    print("Scored Distinction")
elif marks >= 60 and marks < 75:
    print("First Grade")
elif marks >= 55 and marks < 60:
    print("Second Class")
elif marks >= 35 and marks < 55:
    print("Third Class")
else:
    print("Failed")

