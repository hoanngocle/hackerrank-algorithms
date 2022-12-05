

def timeConversion(string):
    string = string.split(":")
    hour = "00"
    if "AM" in string[2]:
        if string[0] == "12": 
            hour = "00"
        else:
            hour = string[0]
        return hour + ":" + string[1] + ":" + string[2].replace("AM", "")
    elif "PM" in string[2]:
        if string[0] == "12": 
            hour = "12"
        else:
            hour = str(int(string[0]) + 12)
        return hour + ":" + string[1] + ":" + string[2].replace("PM", "")

string = "06:40:03AM"
# Call function
output = timeConversion(string)

# Print output
print("==================")
print("Output: " + str(output))