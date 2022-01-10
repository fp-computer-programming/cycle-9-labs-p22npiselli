# Author: Nolan (AMDG) 1/10/2022

def double_stuff(lst):
    for index, value in enumerate(lst):
        lst[index] = 2 * value
    return lst



print(double_stuff([1, 2]) == [2, 4])
print(double_stuff([1.1, 2]) == [2.2, 4])
print(double_stuff(["a", 1]) == ["aa", 2])

