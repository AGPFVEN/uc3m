#Calculator of seconds
#Ask for seconds
sec = int(input("number of seconds: "))

#Compare and calculate
if (sec > 3600):
    hours = int(sec / 3600)
    sec %= 3600 

    if (hours < 10):
        hours = "0" + str(hours)

else:
    hours = "00"

if (sec > 60):
    mins = int(sec / 60)
    sec %= 60

    if (mins < 10):
        mins = "0" + str(mins)

else:
    mins = "00"

if (sec < 10):
    sec = "0" + str(sec)

print(hours, ":", mins, ":", sec)