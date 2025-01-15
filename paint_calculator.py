def main():
    print("Simple Paint Calculator")

    wall_area = float(input("Enter the total area of walls to paint (m²): "))

    include_ceiling = input("Do you want to paint the ceiling? (yes/no): ").strip().lower()
    ceiling_area = 0
    if include_ceiling == "yes":
        ceiling_area = float(input("Enter the area of the ceiling (m²): "))

    obstruction_area = float(input("Enter the total area of obstructions (e.g., windows, doors, radiators) (m²): "))

    total_paintable_area = (wall_area + ceiling_area) - obstruction_area

    paint_coverage = 10  # m² per liter
    paint_cost_per_liter = float(input("Enter the cost of paint per liter (£): "))

    paint_needed = total_paintable_area / paint_coverage
    total_cost = paint_needed * paint_cost_per_liter

    print("\nResults:")
    print(f"Total paintable area: {total_paintable_area:.2f} m²")
    print(f"Paint needed: {paint_needed:.2f} liters")
    print(f"Total cost: £{total_cost:.2f}")


if __name__ == "__main__":
    main()