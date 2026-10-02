# Grab Fare Calculator Logic & CLI-based
# Programmed by: Zainab & Danial Haris

def calculate_fare(distance, vehicle_type, is_peak, passengers):
    # Base fare and rates
    base_fare = 0
    rate_per_km = 0

    if vehicle_type == "GrabCar": # GrabCar
        base_fare = 5.00
        rate_per_km = 1.20
    elif vehicle_type == "GrabCar Plus": # GrabCarPlus
        base_fare = 7.00
        rate_per_km = 1.50
    elif vehicle_type == "GrabCar Premium": # GrabCarPremium
        base_fare = 10.00
        rate_per_km = 2.00
    else:
        return 0, ["Invalid Vehicle Type"]

    # Calculate basic fare
    total_fare = base_fare + (distance * rate_per_km)

    messages = []

    # Peak hour surcharge (e.g., 20% extra)
    if is_peak:
        total_fare = total_fare * 1.20
        messages.append("Peak hour surcharge applied (20%)")

    # Passenger surcharge (e.g., RM1.00 per additional passenger)
    if passengers > 1:
        extra_passenger_fare = (passengers - 1) * 1.00
        total_fare += extra_passenger_fare
        messages.append(f"Additional passenger surcharge applied (RM1.00 per extra passenger)")
        messages.append(f"Extra passenger fee applied: RM {extra_passenger_fare:.2f}")

    return total_fare, messages

def print_header():
    print("=" * 40)
    print("      GRAB FARE CALCULATOR (MALAYSIA)      ")
    print("=" * 40)

def show_vehicle_menu():
    print("\n--- Select Vehicle Type ---")
    print("1. GrabCar")
    print("2. GrabCar Plus")
    print("3. GrabCar Premium")
    print("---------------------------")

def get_vehicle_choice():
    while True:
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            return "GrabCar"
        elif choice == "2":
            return "GrabCar Plus"
        elif choice == "3":
            return "GrabCar Premium"
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def get_distance():
    while True:
        try:
            distance = float(input("Enter distance (km): "))
            if distance <= 0:
                print("Distance must be greater than 0.")
                continue
            return distance
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_passengers():
    while True:
        try:
            passengers = int(input("Enter number of passengers: "))
            if passengers <= 0:
                print("Number of passengers must be a positive integer.")
                continue
            return passengers
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print_header()
    
    show_vehicle_menu()
    vehicle_type = get_vehicle_choice()

    distance = get_distance()
    passengers = get_passengers()

    peak_input = input("Is it Peak Hour? (y/n): ").lower()
    is_peak = peak_input == 'y'

    try:
        passengers = int(input("Enter number of passengers: "))
    except ValueError:
        print("Invalid input. Defaulting to 1 passenger.")
        passengers = 1

    fare, messages = calculate_fare(distance, vehicle_type, is_peak, passengers)
    print(f"The calculated fare is: RM{fare:.2f}")
    for msg in messages:
        print(msg)
    
    print(f"The calculated fare is: RM{fare:.2f}")

if __name__ == "__main__":
    main()