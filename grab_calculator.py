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

if __name__ == "__main__":
    main()