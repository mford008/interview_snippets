# Hackerrank problem objective: find the absolute value of the
# difference between the two diagonal sums in a matrix
# Matrix defined here
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def diagonalDifference(arr):
    # Set variables for each diagonal sum
    d1 = 0
    d2 = 0
    n = len(arr)
    # Loop through each value
    for i in range(n):
        # Picking up array values where each equals its position in the larger array
        d1 += arr[i][i]
        d2 += arr[i][n-1-i]
        # Get absolute difference
        diff = abs(d1 - d2)
    return diff


diagonalDifference(arr)
