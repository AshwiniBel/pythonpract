list=[1,2,3,4,5]
count = 1
for i in list:
    if(i==2):
        print("item matched")
        count = count + 1
        break
print("found at", count, "location")
