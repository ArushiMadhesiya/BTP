import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splprep, splev
from scipy.spatial import Voronoi
from shapely.geometry import Polygon, LineString
import csv

def load_coordinates_from_csv(file_path):
    """
    Load x, y coordinates from a CSV file.
    
    Parameters:
    - file_path: path to the .csv file containing X, Y coordinates.
    
    Returns:
    - x_coords, y_coords: numpy arrays of x and y coordinates.
    """
    data = np.genfromtxt(file_path, delimiter=',', skip_header=1, names=["X", "Y"])
    return data["X"], data["Y"]

def interpolate_curve(x, y, num_points=500):
    """
    Interpolate the curve to generate a smoother representation.
    
    Parameters:
    - x, y: x and y coordinates of the curve.
    - num_points: number of interpolated points.
    
    Returns:
    - interpolated_x, interpolated_y: numpy arrays of interpolated x and y coordinates.
    """
    tck, _ = splprep([x, y], s=0.5, per=True)  # per=True for closed curve
    u = np.linspace(0, 1, num_points)
    interpolated_x, interpolated_y = splev(u, tck)
    return interpolated_x, interpolated_y

def compute_medial_axis_from_polygon(x, y):
    """
    Compute the medial axis of a polygon directly from the coordinates.
    
    Parameters:
    - x, y: x and y coordinates of the polygon boundary.
    
    Returns:
    - polygon: Shapely Polygon object.
    - medial_axis_edges: list of LineString objects representing the medial axis.
    """
    # Create the polygon
    boundary_coords = list(zip(x, y))
    polygon = Polygon(boundary_coords)

    # Compute the Voronoi diagram of the boundary points
    points = np.array(boundary_coords)
    vor = Voronoi(points)

    # Collect the edges that are within the polygon
    medial_axis_edges = []

    # Iterate over Voronoi ridges
    for point_indices, ridge_vertices in zip(vor.ridge_points, vor.ridge_vertices):
        # Check if both vertices are finite
        if ridge_vertices[0] != -1 and ridge_vertices[1] != -1:
            # Get the coordinates of the vertices
            v0 = vor.vertices[ridge_vertices[0]]
            v1 = vor.vertices[ridge_vertices[1]]
            edge = LineString([v0, v1])

            # Check if the edge is entirely within the polygon
            if polygon.contains(edge):
                medial_axis_edges.append(edge)

    return polygon, medial_axis_edges

def plot_medial_axis(polygon, medial_axis_edges):
    """
    Plot the polygon and its medial axis.
    
    Parameters:
    - polygon: Shapely Polygon object.
    - medial_axis_edges: list of LineString objects representing the medial axis.
    """
    fig, ax = plt.subplots()

    # Plot the polygon boundary
    x, y = polygon.exterior.xy
    ax.plot(x, y, 'b', label='Polygon Boundary')

    # Plot the medial axis edges
    for edge in medial_axis_edges:
        x_coords, y_coords = edge.xy
        ax.plot(x_coords, y_coords, 'r', label='Medial Axis' if 'Medial Axis' not in ax.get_legend_handles_labels()[1] else "")

    ax.set_aspect('equal')
    ax.legend()
    plt.show()

# Load coordinates from the .csv file
file_path = 'triangle.csv'  # Update this to the path of your .csv file
x_coords, y_coords = load_coordinates_from_csv(file_path)

# Interpolate the curve for smoothness
interpolated_x, interpolated_y = interpolate_curve(x_coords, y_coords, num_points=1000)

# Compute the Medial Axis Transform directly from the coordinates
polygon, medial_axis_edges = compute_medial_axis_from_polygon(interpolated_x, interpolated_y)

# Plot the polygon and its medial axis
plot_medial_axis(polygon, medial_axis_edges)

# Save medial axis coordinates to a .csv file
with open("medial_axis_coordinates.csv", "w", newline='') as csvfile:
    fieldnames = ['X', 'Y']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for edge in medial_axis_edges:
        x_coords, y_coords = edge.xy
        for x, y in zip(x_coords, y_coords):
            writer.writerow({'X': x, 'Y': y})
