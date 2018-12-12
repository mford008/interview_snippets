arr = [1,2,3,4,5]
a = len(arr)
d = ''
def leftRot(arr, a, d):
    for i in range(d):
        singleleftRotate(a)
    print(arr)

def singleleftRotate(a):
    temp = arr[0]
    for i in range(a-1):
        arr[i] = arr[i+1]
    arr[a-1] = temp


leftRot(arr, 5, 4)


# Alternatively:
# def rotLeft(a, d):
#     a = list(a)
#     return a[d:] + a[:d]
