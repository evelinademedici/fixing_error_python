def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

number_one = int(input("Enter a number: ")) #added int()
number_two = int(input("Enter another number: "))

message = "The result of " + str(number_one) + " + " + str(number_two) + " is " + str(add(number_one, number_two)) # added str()
print(message)

message = "The result of " + str(number_one) + " - " + str(number_two) + " is " + str(subtract(number_one, number_two))   
print(message)