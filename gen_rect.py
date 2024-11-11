def generate_rectangle_coordinates(x1, y1, x2, y2, filename):
    coordinates = []

    # Top edge
    for x in range(x1, x2 + 1):
        coordinates.append((x, y1))
    
    # Bottom edge
    for x in range(x1, x2 + 1):
        coordinates.append((x, y2))
    
    # Left edge
    for y in range(y1 + 1, y2):
        coordinates.append((x1, y))
    
    # Right edge
    for y in range(y1 + 1, y2):
        coordinates.append((x2, y))

    # Write to file
    with open(filename, 'w') as f:
        for coord in coordinates:
            f.write(f"{coord[0]},{coord[1]}\n")

# Define your rectangle's corners
x1, y1 = 50, 50  # Top-left corner
x2, y2 = 100, 100  # Bottom-right corner

# Generate and save the coordinates
generate_rectangle_coordinates(x1, y1, x2, y2, 'myrect1.txt')
