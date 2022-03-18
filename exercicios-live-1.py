# In this code, we have a revision of functions, for (loops), lists and dictionary

# variables


sum = 0


# functions


def function_name():
    print(
        'Hello world! Just testin the execution of this function.'
    )


def sum_of_two_numbers(x, y):
    z = x + y
    return z


def operations(w, h):
    sum_of_two = w + h
    subtraction_of_two = w - h
    return (sum_of_two, subtraction_of_two)


# loop
for i in range(1, 50, 2):
    sum += i  # defined in the beginning

# lists

list_of_vehicles = ["Bycicle", "Train", "Car", "Plane", "Boat"]
list_of_names = []

# dictionary

dictionary_students_grades = {
    "Robert": 8.0,
    "Steve": 6.0,
    "Patrick": 4.5,
    "Mathew": 1.0
}

empty_dictionary = {}

# show in screen the result of the above

print(
    "The result of the sum of 1 + 3 + 5 + 7 + ... + 49 is:", sum
)

a = int(
    input(
        "Please, inform the value of a: "
    )
)
b = int(
    input(
        "Please, inform the value of b: "
    )
)
c = sum_of_two_numbers(a, b)
print(
    "The result of the sum of a + b is:", c
)

d = int(
    input(
        "Please, inform the value of d: "
    )
)
e = int(
    input(
        "Please, inform the value of e: "
    )
)
results = operations(d, e)
print(
    "The result of the sum of d + e is: ", results[0]
)
print(
    "The result of the subtraction of d - e is: ", results[1]
)

print(
    "Check the list of vehicles bellow:"
)
print(list_of_vehicles)
print(
    "Now let's add a vehicle to this list:"
)
list_of_vehicles.append("Motorcycle")
print(list_of_vehicles)

user_vehicle = input(
    "Now answer me this question: What vehicle do you use the most on a daily basis? \n"
)
if user_vehicle in list_of_vehicles:
    print(
        "This vehicle is already in our list!"
    )
else:
    print(
        "Great, we did not have this vehicle in our list, we will add to it! Check the complete updated list bellow:"
    )
    list_of_vehicles.append(user_vehicle)
    print(list_of_vehicles)

for i in range(5):
    name = input(
        "Please, inform us your name: "
    )
    list_of_names.append(name)
print(
    "The list of names collected from the user is: \n", list_of_names
)

print(
    "Robert's grade is: ", dictionary_students_grades["Robert"], ".",
    "\n",
    "Steve's grade is: ", dictionary_students_grades["Steve"], "."
)

dictionary_students_grades["Bruce"] = 7.4

print(
    "Bruce's grade is: ", dictionary_students_grades["Bruce"]
)

for i in range(5):
    key = input(
        "Please, inform us a key: "
    )
    value = float(
        input(
            "Please, inform us a value: "
        )
    )
    empty_dictionary[key] = value

print(
    empty_dictionary
)

verify_name = input(
    "Tell us the name that you want to verify: "
)
if verify_name in dictionary_students_grades:
    print(
        "Oh yeah, we already have your grade! It's: ", dictionary_students_grades[verify_name]
    )
else:
    print(
        "You'll have to wait, we did not had time to compute your grades!"
    )
