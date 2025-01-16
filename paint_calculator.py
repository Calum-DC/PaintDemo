def totalWallArea():
    wall_area = 0
    while True:
        try:
            print("Please enter the dimensions of the wall you wish to paint")
            wall_length = float(input("Enter the length of the wall (m): "))
            wall_height = float(input("Enter the height of the wall (m): "))
            if wall_height <= 0 or wall_length <= 0:
                print("Dimensions must be positive, please try again")
                continue
            wall_area += wall_length * wall_height
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        else:
            add_another_wall = input("Do you want to add another wall? (yes/no): ").strip().lower()
            if add_another_wall != "yes" and add_another_wall != "y":
                break
    return wall_area

def totalCeilingArea():
    ceiling_area = 0
    ceiling = input("Do you want to paint the ceiling? (yes/no): ").strip().lower()
    if ceiling in ("yes","y"):
        while True:
            try:
                ceiling_width = float(input("Enter the width of the ceiling (m): "))
                ceiling_depth = float(input("Enter the depth of the ceiling (m): "))
                if ceiling_depth <= 0 or ceiling_width <=0:
                    print("Dimensions must be positive, please try again")
                    continue
                ceiling_area = ceiling_depth * ceiling_width
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
    return ceiling_area

def totalObstructionArea():
    while True:
        try:
            obstructions = float(input("Enter the total area of obstructions (e.g., windows, doors, radiators) (m²): "))
            return obstructions
        except ValueError:
            print("Invalid input. Please enter a number.")

def whatPaint():
    print("Please choose the type of paint you wish to use:")
    print("1. Low-end paint (£4 per litre)")
    print("2. Mid-range paint (£10 per litre)")
    print("3. High-end paint (£20 per litre)")

    while True:
        paint_choice = int(input("Which Paint would you like to use? (Please enter 1,2 or 3): "))
        if paint_choice == 1:
            return 4
        elif paint_choice == 2:
            return 10
        elif paint_choice == 3:
            return 20
        else:
            print("Invalid choice, please enter 1, 2, or 3")

def paintName(paint_cost_per_litre):
    if paint_cost_per_liter == 4:
        return "Low-end Paint"
    elif paint_cost_per_liter == 10:
        return "Mid-range Paint"
    elif paint_cost_per_liter == 20:
        return "High-end Paint"

if __name__ == "__main__":
    print("Simple Paint Calculator \n")

    #couple of functions
    total_wall_area = totalWallArea()
    print("\n")
    total_ceiling_area = totalCeilingArea()
    print("\n")
    total_obstruction_area = totalObstructionArea()
    print("\n")

    total_paintable_area = (total_wall_area + total_ceiling_area) - total_obstruction_area

    paint_coverage = 10  # m² per liter
    paint_cost_per_liter = whatPaint()

    paint_needed = total_paintable_area / paint_coverage
    total_cost = paint_needed * paint_cost_per_liter
    paint_type = paintName(paint_cost_per_liter)

    print("\nResults:")
    print(f"Total paintable area: {total_paintable_area:.2f} m²")
    print(f"Paint needed: {paint_needed:.2f} liters")
    print(f"Paint type: {paint_type}")
    print(f"Total cost: £{total_cost:.2f}")
