#include <iostream>

struct Rectangle {
    double width, height;
    
    double verticalMedialAxis() {
        return width / 2;
    }
    
    double horizontalMedialAxis() {
        return height / 2;
    }
};

int main() {
    Rectangle rect = {10, 5};
    std::cout << "Vertical Medial Axis (x): " << rect.verticalMedialAxis() << std::endl;
    std::cout << "Horizontal Medial Axis (y): " << rect.horizontalMedialAxis() << std::endl;
    return 0;
}
