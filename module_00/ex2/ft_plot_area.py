def ft_plot_area():
    length: str = input("Enter length: ")
    width: str = input("Enter width: ")
    try:
        print("Plot area:", (int(length) * int(width)))
    except ValueError:
        print("Calculation failed, please enter numbers only")
