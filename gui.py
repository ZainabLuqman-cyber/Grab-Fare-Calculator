import tkinter as tk
from tkinter import ttk
from grab_calculator import calculate_fare   # <-- Import the shared function

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

def calculate():
    try:
        distance = float(distance_entry.get())
        passengers = int(passenger_choice.get())
        vehicle_type = vehicle_choice.get()

        if distance <= 0 or passengers < 1 or not vehicle_type:
            raise ValueError

        fare, messages = calculate_fare(distance, vehicle_type, peak_var.get(), passengers)
        result_label.config(text=f"Estimated Fare: RM {fare:.2f}")
        message_label.config(text="\n".join(messages))
    except ValueError:
        result_label.config(text="Please enter valid fare details.")

result_label = tk.Label(
    window,
    text="",
    font=("Arial", 12, "bold"),
)
result_label.pack(pady=5)

message_label = tk.Label(
    window,
    text="",
    font=("Arial", 10),
    wraplength=400,
    justify="center"
)

message_label.pack(pady=5)

calculate_button = tk.Button(
    window,
    text="Calculate Fare",
    font=("Arial", 12, "bold"),
    command=calculate
    
)
calculate_button.pack(pady=20)

# Run the window
window.mainloop()