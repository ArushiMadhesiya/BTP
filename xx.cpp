#include <iostream>
#include <cmath>

struct Point {
    double x, y;
};

double distance(Point p1, Point p2) {
    return sqrt(pow(p2.x - p1.x, 2) + pow(p2.y - p1.y, 2));
}

int main() {
    Point p1 = {0, 0};
    Point p2 = {3, 4};
    
    std::cout << "Distance: " << distance(p1, p2) << std::endl;
    return 0;
}
