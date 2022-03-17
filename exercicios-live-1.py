# variables


sum = 0


# functions


def function_name():
    print('Hello world! Just testin the execution of this function ;)')


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


# show in screen the result of the above

print("The result of the sum of 1 + 3 + 5 + 7 + ... + 49 is:", sum)

a = int(input("Please, inform the value of a: "))
b = int(input("Please, inform the value of b: "))
c = sum_of_two_numbers(a, b)
print("The result of the sum of a + b is:", c)

d = int(input("Please, inform the value of d: "))
e = int(input("Please, inform the value of e: "))
results = operations(d, e)
print("The result of the sum of d + e is: ", results[0])
print("The result of the subtraction of d - e is: ", results[1])
