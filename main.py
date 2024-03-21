from square_generator.square_generator import CubicGenerator
import math
####1
# Task 1: Generate squares of numbers 1 through 10 using list comprehension
squares = [x**2 for x in range(1, 11)]
print("Squares from 1 to 10:", squares)

# Task 2: Define a function to calculate squares in a given range
def generate_squares(start, end):
    return [x**2 for x in range(start, end + 1)]

# Use the function to generate squares of numbers 1 through 5
print("Squares from 1 to 5 using function:", generate_squares(1, 5))

# Task 3 & 8: Use the CubicGenerator class to generate cubes
cubic_gen = CubicGenerator()
cubes = cubic_gen.generate_squares(1, 5)
print("Cubes from 1 to 5:", cubes)

# Task 4: Use the math library to calculate square roots of the cubes generated
def calculate_square_roots(numbers):
    return [math.sqrt(number) for number in numbers]

cube_roots = calculate_square_roots(cubes)
print("Cube roots of cubes from 1 to 5:", cube_roots)
