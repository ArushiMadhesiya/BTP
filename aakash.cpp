#include <iostream>
#include <vector>


using namespace std;

// Structure to represent a point in 2D space
struct Point {
    double x, y;
};

// Function to calculate the medial axis with multiple points
vector<Point> findMedialAxis(const vector<Point>& boundarypoints, int numPoints){
  // Initialize minimum and maximum values for x and y coordinates
    double minX = boundarypoints[0].x;
    double maxX = boundarypoints[0].x;
    double minY = boundarypoints[0].y;
    double maxY = boundarypoints[0].y;
    
    // Find the minimum and maximum x and y coordinates using std::min and std::max
    for (const auto& point : boundarypoints) {
        minX = min(minX, static_cast<double>(point.x));
        maxX = max(maxX, static_cast<double>(point.x));
        minY = min(minY, static_cast<double>(point.y));
        maxY = max(maxY, static_cast<double>(point.y));
    }
    
    
    // The medial axis is the line passing through the middle of the rectangle
    double medialY = (minY + maxY) / 2;
    
    // Generate multiple points along the medial axis
    vector<Point> medialAxisPoints;
    double step = (maxX - minX) / (numPoints - 1); // Calculate the step size between points

    for (int i = 0; i < numPoints; ++i) {
        Point medialPoint;
        medialPoint.x = minX + i * step;
        medialPoint.y = medialY;
        medialAxisPoints.push_back(medialPoint);
    }
    
    return medialAxisPoints;
}

int main() {
    // Define multiple points representing the boundary of the rectangle
    vector<Point> boundarypoints = {
        {0.0, 0.0}, {0.0, 1.0}, {0.0, 2.0}, {0.0, 3.0}, {0.0, 4.0},  // Left boundary
        {6.0, 0.0}, {6.0, 1.0}, {6.0, 2.0}, {6.0, 3.0}, {6.0, 4.0},  // Right boundary
        {1.0, 0.0}, {2.0, 0.0}, {3.0, 0.0}, {4.0, 0.0}, {5.0, 0.0},  // Bottom boundary
        {1.0, 4.0}, {2.0, 4.0}, {3.0, 4.0}, {4.0, 4.0}, {5.0, 4.0}   // Top boundary
    };
    
    // Find and display the medial axis with multiple points
    int numPointsOnMedialAxis = 10;  // For example, we can calculate 10 points along the medial axis
    vector<Point> medialAxisPoints = findMedialAxis(boundarypoints, numPointsOnMedialAxis);
    
    cout << "Medial Axis Points:" << endl;
    for (const auto& p : medialAxisPoints) {
        cout << "(" << p.x << ", " << p.y << ")" << endl;
    }

    return 0;
}