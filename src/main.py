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
