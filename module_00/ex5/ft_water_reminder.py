WATER_REMINDER_DAYS = 2

def ft_water_reminder():
    last_watering = int(input("Days since last watering: "))
    if last_watering > WATER_REMINDER_DAYS:
        print("Water the plants!")
    else:
        print("Plants are fine")