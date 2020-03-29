def nearthousand(n) :
    return((abs(1000-n) <= 100) or (abs(2000-n) <= 100))
print(nearthousand(1000))
print(nearthousand(900))
print(nearthousand(800))
print(nearthousand(2200))
