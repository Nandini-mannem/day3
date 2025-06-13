# Function without parameter
def greet_user():
    return "Welcome"

print(greet_user())


def add_numbers(num1, num2):
    print(num1, num2)

add_numbers(10, 20)


# Default parameters
def user_profile(username, userage, usergender="Male"):
    print(f"Username: {username}, Age: {userage}, Gender: {usergender}")

user_profile("Rahul", 30)


# Arbitrary arguments
def favorite_fruits(*fruits):
    print(fruits)

favorite_fruits("Apple", "Banana", "Mango", "Orange")


# Keyword arguments
def travel_details(name,age,seats):
    print(f"Name: {name}, Age: {age}, Seats: {seats}")

print(travel_details(name="nandu",age=21, seats=2))


# Keyword arbitrary arguments
def city_info(**info):
    print(info)

city_info(City="Mumbai", Population="20M", Country="India")


# Lambda function
cube = lambda n: n**3
print(cube(4))