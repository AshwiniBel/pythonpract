#Sum of all items of list
def sum_list(items):
    sum_numbers=0
    for x in items:
        sum_numbers+= x
    return sum_numbers
print(sum_list([1,2,4]))

#Multiply List
def multi_list(items):
    multi_nums=1
    for x in items:
        multi_nums*=x
    return multi_nums
print(multi_list([1,2,4]))

