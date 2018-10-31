from random import randint

array = [5,9,1,6,2,3,8]
print(array)

def quick(array):
    if len(array) <= 1:
        return array
    smaller, equal, greater = [], [], []
    pivot = array[randint(0, len(array)-1)]
    for x in array:
        if x > pivot:
            greater.append(x)
        elif x == pivot:
            equal.append(x)
        elif x < pivot:
            smaller.append(x)
    return quick(smaller) + equal + quick(greater)

s = quick(array)
print(s)
