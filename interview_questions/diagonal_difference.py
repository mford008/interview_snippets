arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def diagonalDifference(arr):
    d1 = 0
    d2 = 0
    n = len(arr)
    for i in range(n):
        d1 += arr[i][i]
        d2 += arr[i][n-1-i]
        diff = abs(d1 - d2)
    return diff


diagonalDifference(arr)
