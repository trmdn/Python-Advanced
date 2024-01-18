number = int(input())

car_lots = set()

for _ in range(number):
    data = input().split(", ")
    command, car_numbers = data
    
    if command == "IN":
        car_lots.add(car_numbers)
    elif command == "OUT":
        if car_numbers in car_lots:
            car_lots.remove(car_numbers)

if car_lots:
    for car in car_lots:
        print(car)
else:
    print("Parking Lot is Empty")