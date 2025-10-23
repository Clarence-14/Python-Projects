# a program that takes a user’s input as a string, converts it to different data types and performs operations to demonstrate type effects.

import math

user_input = input("Enter a number:")

converted_int = int(user_input)
converted_float = float(user_input)

sum_float = (converted_float + 10) * 2
sum_int = (converted_int + 10) * 2

type_int = type(converted_int)
type_float = type(converted_float)

print(f"The integer value is {sum_int} and its type is {type_int}")
print(f"The float value is {sum_float} and its type is {type_float}") 