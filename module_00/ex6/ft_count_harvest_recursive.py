def ft_count_harvest_recursive(current_day: int = 1):
    if current_day <= days_until_harvest:
        print(f"Day {current_day}")
        return (ft_count_harvest_recursive(current_day + 1))
    else:
        print("Harvest time!")
        return
    

days_until_harvest = int(input("Days until harvest: "))
