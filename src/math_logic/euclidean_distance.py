import math

# Define the coordinates of the two points
point1 = (2, 3)
point2 = (10, 8)

# Extract x and y coordinates
x1, y1 = point1
x2, y2 = point2

# Calculate the differences
diff_x = x2 - x1
diff_y = y2 - y1

# Calculate the squared differences
squared_diff_x = diff_x**2
squared_diff_y = diff_y**2

# Calculate the sum of squared differences
sum_of_squared_diffs = squared_diff_x + squared_diff_y

# Calculate the square root
euclidean_distance = math.sqrt(sum_of_squared_diffs)

print(f"The Euclidean distance between {point1} and {point2} is: {euclidean_distance}")

# You can also define a function for reusability:
def calculate_euclidean_distance(p1, p2):
    """
    Calculates the Euclidean distance between two 2D points.

    Args:
        p1 (tuple): A tuple representing the first point (x1, y1).
        p2 (tuple): A tuple representing the second point (x2, y2).

    Returns:
        float: The Euclidean distance between the two points.
    """
    x1, y1 = p1
    x2, y2 = p2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Test the function
distance_calculated = calculate_euclidean_distance((2, 3), (10, 8))
print(f"Using function: The Euclidean distance is: {distance_calculated}")
