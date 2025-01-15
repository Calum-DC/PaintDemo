def totalWallArea():
    wall_area = 0
    while True:
        try:
            print("Please enter the dimensions of the first wall you wish to paint")
            wall_length = float(input("Enter the length of the wall (m): "))
            wall_height = float(input("Enter the height of the wall (m): "))
            wall_area += wall_length * wall_height
        except ValueError:
            print("Invalid input. Please enter a number.")
        else:
            add_another_wall = input("Do you want to add another wall? (yes/no): ").strip().lower()
            if add_another_wall != "yes" and add_another_wall != "y":
                break
    return wall_area


def totalCeilingArea():
    ceiling_area = 0
    ceiling = input("Do you want to paint the ceiling? (yes/no): ").strip().lower()
    try:
        if ceiling != "yes" and "y":
            ceiling_area = float(input("Enter the area of the ceiling (m²): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
    return ceiling_area


if __name__ == "__main__":
    print("Simple Paint Calculator")

    #couple of functions
    total_wall_area = totalWallArea()

    total_ceiling_area = totalCeilingArea()

    obstruction_area = float(input("Enter the total area of obstructions (e.g., windows, doors, radiators) (m²): "))

    total_paintable_area = (total_wall_area + total_ceiling_area) - obstruction_area

    paint_coverage = 10  # m² per liter
    paint_cost_per_liter = float(input("Enter the cost of paint per liter (£): "))

    paint_needed = total_paintable_area / paint_coverage
    total_cost = paint_needed * paint_cost_per_liter

    print("\nResults:")
    print(f"Total paintable area: {total_paintable_area:.2f} m²")
    print(f"Paint needed: {paint_needed:.2f} liters")
    print(f"Total cost: £{total_cost:.2f}")
