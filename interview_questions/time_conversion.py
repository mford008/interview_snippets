# Set test values of s
s = "07:05:49PM"
# s = "12:40:00PM"
# s = "07:05:49AM"

def timeConversion(s):
    # Set variable for only hour since only the hour changes
    hour = s[:2]
    # Separate AM and PM times
    if s[8:] == "AM":
        # Identify special cases
        if hour == "12":
            military_hour = "00"
            military_time = str(military_hour) + s[2:]
            return str(military_time[:8])
        # Leave all other cases as they are minus AM PM distinction
        else:
            return s[:8]
    elif s[8:] == "PM":
        if hour == "12":
            return s[:8]
        else:
            military_hour = 12 + int(hour)
            military_time = str(military_hour) + s[2:]
            return str(military_time[:8])


timeConversion(s)
