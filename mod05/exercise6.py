import random

random_points = int(input("Enter a number of random points to generate: "))

generated_points = 0
points_inside_circle = 0 

while generated_points < random_points: 
    coordinate_x = random.uniform(-1, 1)
    coordinate_y = random.uniform(-1, 1)
    if coordinate_x ** 2 + coordinate_y ** 2 < 1:
        points_inside_circle = points_inside_circle + 1
    generated_points = generated_points + 1

approximate_pi = 4 * points_inside_circle / generated_points

print(f"The approximation of pi is {approximate_pi}.")