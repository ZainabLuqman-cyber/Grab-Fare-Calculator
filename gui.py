import tkinter as tk
from tkinter import ttk


# Create the main window
window = tk.Tk()

# Window title
window.title("Grab Fare Calculator")
window.geometry("500x600")
window.resizable(False, False)

title = tk.Label(
    window,
    text="Grab Fare Calculator",
    font=("Arial", 24, "bold"),
)

title.pack(pady=20)

subtitle = tk.Label(
    window,
    text="Calculate your Grab fare easily!",
    font=("Arial", 12),
)

subtitle.pack(pady=10)

vehicle_label = tk.Label(
    window,
    text="Select Vehicle Type:",
    font=("Arial", 12),
)

vehicle_label.pack(pady=(30, 5))

vehicle_choice = ttk.Combobox(
    window,
    values=[
        "GrabCar",
        "GrabCar Plus", 
        "GrabCar Premium"
        ],
    state="readonly",
)
    
vehicle_choice.pack(pady=10)

distance_label = tk.Label(
    window,
    text="Enter Distance (km):",
    font=("Arial", 12),
)

distance_label.pack(pady=(20, 5))

distance_entry = tk.Entry(
    window,
    font=("Arial", 12),
)

distance_entry.pack(pady=10)

peak_var = tk.BooleanVar()
peak_checkbox = tk.Checkbutton(
    window,
    text="Peak Hour",
    font=("Arial", 12),
    variable=peak_var
)

peak_checkbox.pack(pady=20)

passenger_label = tk.Label(
    window,
    text="Number of Passengers:",
    font=("Arial", 12),
)
passenger_label.pack(pady=(10, 5))

passenger_choice = ttk.Combobox(
    window,
    values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    state="readonly",
)
passenger_choice.pack()

def calculate_fare(distance, vehicle_type, is_peak, passengers):
    # Base fare and rates
    base_fare = 0
    rate_per_km = 0

    if vehicle_type == "GrabCar":
        base_fare = 5.00
        rate_per_km = 1.20
    elif vehicle_type == "GrabCar Plus":
        base_fare = 7.00
        rate_per_km = 1.50
    elif vehicle_type == "GrabCar Premium":
        base_fare = 10.00
        rate_per_km = 2.00
    else:
        return "Invalid Vehicle Type"

    # Calculate basic fare
    total_fare = base_fare + (distance * rate_per_km)

    # Peak hour surcharge (e.g., 20% extra)
    if is_peak:
        total_fare = total_fare * 1.20

    # Passenger surcharge (e.g., RM1.00 per additional passenger)
    if passengers > 1:
        extra_passenger_fare = (passengers - 1) * 1.00
        total_fare += extra_passenger_fare

    return total_fare   

def calculate():
    try:
        distance = float(distance_entry.get())
        passengers = int(passenger_choice.get())
        vehicle_type = vehicle_choice.get()

        if distance < 0 or passengers < 1 or not vehicle_type:
            raise ValueError

        fare = calculate_fare(distance, vehicle_type, peak_var.get(), passengers)
        result_label.config(text=f"Estimated Fare: RM {fare:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid fare details.")

result_label = tk.Label(
    window,
    text="",
    font=("Arial", 12, "bold"),
)
result_label.pack(pady=5)

calculate_button = tk.Button(
    window,
    text="Calculate Fare",
    font=("Arial", 12, "bold"),
    command=calculate
    
)
calculate_button.pack(pady=20)

# Run the window
window.mainloop()