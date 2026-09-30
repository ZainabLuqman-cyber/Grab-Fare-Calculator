print("Grab Ride Fare Calculator")
print("----------------------------")

print("1. GrabCar")
print("2. GrabCar Plus")
print("3. GrabCar Premium")

ride_type = int(input("Enter your ride type: "))

if ride_type == 1:
    ride_name = "GrabCar"
    base_fare = 5.00
    per_km_ = 1.20
elif ride_type == 2:
    ride_name = "GrabCar Plus"
    base_fare = 7.00
    per_km_ = 1.50
elif ride_type == 3:
    ride_name = "GrabCar Premium"
    base_fare = 10.00
    per_km_ = 2.00  
else:
    ride_name = "Invalid ride type"
    base_fare = 0.00
    per_km_ = 0.00

print("You selected option:", ride_name)

distance = float(input("Enter travel distance (km): "))

print("Distance:", distance, "km")
print("Base Fare: RM", base_fare)
print("Rate per km: RM", per_km_)

print()
print("1. Peak Hours")
print("2. Off-Peak Hours")

time_type = int(input("Enter your time period: "))

if time_type == 1:
    peak_multiplier = 1.20
    period_name = "Peak Hours"
elif time_type == 2:
    peak_multiplier = 1.00
    period_name = "Off-Peak Hours"
else:
    peak_multiplier = 1.00
    period_name = "Off-Peak Hours"

print("Time period:", period_name)

estimated_fare = base_fare + (per_km_ * distance)
estimated_fare = estimated_fare * peak_multiplier
print("Estimated Fare: RM", round(estimated_fare, 2))

passengers = int(input("Enter number of passengers: "))
if passengers > 4:
    print("Additional charge for extra passengers.")
    extra_passengers = passengers - 4
    extra_charge = extra_passengers * 2.00
    estimated_fare += extra_charge
    print("Extra charge for", extra_passengers, "extra passengers: RM", round(extra_charge, 2))

print("Passenger charge: RM", round(estimated_fare, 2))