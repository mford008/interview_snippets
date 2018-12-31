# This problem was taken from the Birthday Cake Candles problem on Hackerrank

def birthdayCakeCandles(ar):
    # Find the candle with the maximum height by using built-in python functions
    # to find the max in the list
    max_height = max(ar)
    # Use python's count method to count the occurrences of our max height variable
    candle_count = ar.count(max_height)
    # print or return the value
    print(candle_count)
