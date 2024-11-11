#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main(int argc, char** argv) {
    // Read the input image
    Mat img = imread("input_image.png", IMREAD_GRAYSCALE);
    
    if (img.empty()) {
        cout << "Could not open or find the image!" << endl;
        return -1;
    }

    // Convert to binary image (thresholding)
    Mat binImg;
    threshold(img, binImg, 127, 255, THRESH_BINARY);

    // Invert the binary image (to ensure the object is white and background is black)
    Mat binImgInv;
    bitwise_not(binImg, binImgInv);

    // Initialize the skeleton
    Mat skel(binImgInv.size(), CV_8UC1, Scalar(0));
    Mat temp;
    Mat eroded;
    Mat dilated;

    // Create the structuring element (3x3 cross-shaped kernel)
    Mat element = getStructuringElement(MORPH_CROSS, Size(3, 3));

    bool done = false;
    while (!done) {
        // Erode the image
        erode(binImgInv, eroded, element);

        // Dilate the eroded image
        dilate(eroded, dilated, element);

        // Subtract the dilated image from the original binary image to get the skeleton
        subtract(binImgInv, dilated, temp);

        // OR the result with the accumulated skeleton
        bitwise_or(skel, temp, skel);

        // Update the binary image for the next iteration
        eroded.copyTo(binImgInv);

        // Check if the image has been fully eroded (done condition)
        done = (countNonZero(binImgInv) == 0);
    }

    // Invert back the skeleton image (so skeleton appears in white)
    bitwise_not(skel, skel);

    // Show the result
    imshow("Skeleton", skel);
    waitKey(0);

    return 0;
}
