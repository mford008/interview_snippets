array = [1,2,4,5,6]
def find_missing_number(array):
    l = len(array)
    theoretical_total = (l+1)*(l+2)/2
    actual_total = sum(array)
    missing_number = theoretical_total - actual_total
    print(missing_number)
find_missing_number(array)
