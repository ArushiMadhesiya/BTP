import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay, Voronoi, voronoi_plot_2d


def load_coordinates_from_csv(file_path):
    """
    Load x, y coordinates from a CSV file.

    Parameters:
    - file_path: path to the .csv file containing X, Y coordinates.

    Returns:
    - points: Numpy array of points (N x 2) where each row is (x, y).
    """
    data = np.genfromtxt(file_path, delimiter=',', skip_header=1, names=["X", "Y"])
    points = np.column_stack((data["X"], data["Y"]))
    return points


def compute_medial_axis_from_coordinates(points):
    """
    Compute the medial axis directly from coordinates using Voronoi diagram.

    Parameters:
    - points: Numpy array of shape (N, 2), representing the coordinates.

    Returns:
    - medial_axis_points: List of points representing the medial axis.
    """
    # Perform Delaunay triangulation
    delaunay = Delaunay(points)

    # Compute Voronoi diagram from Delaunay triangulation
    voronoi = Voronoi(points)

    # Extract Voronoi vertices inside the convex hull
    medial_axis_points = []
    for simplex in delaunay.simplices:
        region = voronoi.regions[voronoi.point_region[simplex[0]]]
        if region != -1 and all(v >= 0 for v in region):
            vertices = voronoi.vertices[region]
            medial_axis_points.extend(vertices)

    return np.array(medial_axis_points)


def plot_medial_axis(points, medial_axis_points):
    """
    Plot the input points, Delaunay triangulation, and the medial axis.

    Parameters:
    - points: Numpy array of shape (N, 2), representing the original points.
    - medial_axis_points: Numpy array of shape (M, 2), representing the medial axis points.
    """
    # Plot original points
    plt.figure(figsize=(8, 8))
    plt.plot(points[:, 0], points[:, 1], 'o', label="Input Points")

    # Compute and plot Voronoi diagram
    vor = Voronoi(points)
    voronoi_plot_2d(vor, show_vertices=False, line_colors='orange', line_width=1, show_points=False)

    # Plot medial axis points
    plt.plot(medial_axis_points[:, 0], medial_axis_points[:, 1], 'rx', label="Medial Axis Points")

    plt.legend()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Medial Axis Transform (MAT)")
    plt.show()


# Load coordinates from CSV
file_path = 'curve.csv'  # Update this to the path of your curve.csv file
points = load_coordinates_from_csv(file_path)

# Compute medial axis directly from coordinates
medial_axis_points = compute_medial_axis_from_coordinates(points)

# Save medial axis points to a file
output_file = "direct_medial_axis_coords.txt"
np.savetxt(output_file, medial_axis_points, delimiter=',', header="X,Y", comments="")
print(f"Medial axis coordinates saved to {output_file}")

# Plot medial axis
plot_medial_axis(points, medial_axis_points)
