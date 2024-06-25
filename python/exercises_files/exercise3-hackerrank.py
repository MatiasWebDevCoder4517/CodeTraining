#### look at the exercise3-hackerrank.png image in folder exercises_images ####


def timeConversion(s):
    # Extract the period (AM/PM)
    period = s[-2:]
    
    # Extract the hour, minute, and second
    hour = s[:2]
    minute = s[3:5]
    second = s[6:8]

    # Convert the hour based on the period
    if period == "AM":
        if hour == "12":
            hour = "00"  # Midnight case
        # Otherwise, hour remains the same for AM
        
    else:  # PM case
        if hour != "12":
            hour = str(int(hour) + 12)  # Convert PM hour to 24-hour format

    # Construct the final 24-hour format time string
    return f"{hour}:{minute}:{second}"

# Example usage:
sample_input = "07:05:45PM"
print(timeConversion(sample_input))  # Should print "19:05:45"

