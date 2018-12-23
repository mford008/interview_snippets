# Set equal to test value
n = 6


def staircase(n):
    # use range of 1 to n because we don't want a blank line on top
    for each in range(1, n + 1):
        # use single print statement to print number of spaces plus hash
        print(' ' * (n - each) + '#' * each)


staircase(n)
