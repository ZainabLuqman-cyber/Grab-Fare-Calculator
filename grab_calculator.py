def calculate_fare(distance, vehicle_type, is_peak, passengers):
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

    # Calculate basic fare
    total_fare = base_fare + (distance * rate_per_km)

    # Peak hour surcharge (e.g., 20% extra)
    if is_peak:
        total_fare = total_fare * 1.20
        print("Peak hour surcharge applied (20%)")

    # Passenger surcharge (e.g., RM1.00 per additional passenger)
    if passengers > 1:
        extra_passenger_fare = (passengers - 1) * 1.00
        total_fare += extra_passenger_fare
        print(f"Additional passenger surcharge applied (RM1.00 per extra passenger)")
        print(f"Extra passenger fee applied: RM {extra_passenger_fare:.2f}")

    return total_fare

def main():
    print("--- Grab Fare Calculator ---")
    
    while True:
        try:
            # Inputs
            distance = float(input("Enter distance (km): "))
            if distance <= 0:
                print("Distance must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    vehicle_type = input("Enter vehicle type (1 for GrabCar, 2 for GrabBike, 3 for GrabTaxi): ")
    
    peak_input = input("Is it Peak Hour? (y/n): ").lower()
    is_peak = peak_input == 'y'

    try:
        passengers = int(input("Enter number of passengers: "))
    except ValueError:
        passengers = 1

    fare = calculate_fare(distance, vehicle_type, is_peak, passengers)
    
    print(f"The calculated fare is: RM{fare:.2f}")

if __name__ == "__main__":
    main()