def calculate_fare(distance, vehicle_type):
    # Base fare and rates
    base_fare = 0
    rate_per_km = 0

    if vehicle_type == "1": # GrabCar
        base_fare = 5.00
        rate_per_km = 1.50
    elif vehicle_type == "2": # GrabBike
        base_fare = 2.00
        rate_per_km = 0.80
    elif vehicle_type == "3": # GrabTaxi
        base_fare = 4.00
        rate_per_km = 1.20
    else:
        return "Invalid Vehicle Type"

    fare = base_fare + (distance * rate_per_km)
    return fare

def main():
    print("--- Grab Fare Calculator ---")
    
    while True:
        try:
            # Inputs
            distance = float(input("Enter distance (km): "))
            vehicle_type = input("Enter vehicle type (1 for GrabCar, 2 for GrabBike, 3 for GrabTaxi): ")
            if distance <= 0:
                print("Distance must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    fare = calculate_fare(distance, vehicle_type)
    print(f"The calculated fare is: ${fare:.2f}")

if __name__ == "__main__":
    main()