arr = [1,1,0,-1,-1]
def plus_minus(arr):
    pos = 0
    neg = 0
    zero = 0
    for each in arr:
        if each == 0:
            zero += 1
        elif each > 0:
            pos += 1
        elif each < 0:
            neg += 1
    print(str.format('{0:.6f}', pos/len(arr)))
    print(str.format('{0:.6f}', neg/len(arr)))
    print(str.format('{0:.6f}', zero/len(arr)))
plus_minus(arr)
