def is_group_member(group_data, n):
    for value in group_data:
        if n == value:
            return true
    return false
print(is_group_member([1,5,8,3],3))
print(is_group_member([5,8,3],-1))            