print("Grab Ride Fare Calculator")
print("----------------------------")

print("1. GrabCar")
print("2. GrabCar Plus")
print("3. GrabCar Premium")

ride_type = int(input("Enter your ride type: "))

if ride_type == 1:
    ride_name = "GrabCar"
elif ride_type == 2:
    ride_name = "GrabCar Plus"
elif ride_type == 3:
    ride_name = "GrabCar Premium"
else:
    ride_name = "Invalid ride type"

print("You selected option:", ride_name)

