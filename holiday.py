city_flight = input("Enter the City you are traveling to:")
num_nights = int(input("Enter the amount of nights you will stay:"))
rental_days = int(input("Enter the number of days you will be renting a car:"))


def hotel_cost(num_nights):
    return num_nights * 1250


def plane_cost(city_flight):
    city_flight = city_flight.lower()
    if city_flight == "mbombela":
        return 3400
    elif city_flight == "cape town":
        return 1800
    elif city_flight == "durban":
        return 2000
    else:
        return 0


def car_rental(rental_days):
    daily_cost = 500
    total_cost = rental_days * daily_cost
    return total_cost


def holiday_cost(num_nights, city_flight, rental_days):
    hotel_total = hotel_cost(num_nights)
    flight_total = plane_cost(city_flight)
    car_total = car_rental(rental_days)
    total = hotel_total + flight_total + car_total
    return total


total_cost = holiday_cost(num_nights, city_flight, rental_days)

print("Holiday details")
print("City:", city_flight)
print("Number of nights:", num_nights)
print("Rental days:", rental_days)
print("Total holiday cost: R", total_cost)
