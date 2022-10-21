angle = int(input("Type angle in degrees: "))
angleMin = angle % 30  # 30 degrees == 1 hour

if angleMin != 0:  # If it shows also minutes
    h = (angle - angleMin) / 30  # Subtract minutes and get hours
    m = angleMin * 2  # Get minutes
    angleMin *= 12  # Get minutes angle
    print("\nMinute hand angle: ", angleMin)
    print("Hours: ", int(h), "Minutes: ", m)
else:  # If it shows 0 minutes
    h = angle // 30
    m = 0
    print("\nMinute hand angle is ", angleMin)
    print("Hours: ", int(h), "Minutes: ", m)
