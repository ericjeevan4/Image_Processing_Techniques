# Image Processing Techniques

## Student Details

**Name:** Eric Jeevan A  
**Register Number:** 312323243043  
**Department:** B.Tech Artificial Intelligence and Data Science

---

## Project Title

Classical Filtering Techniques, Thresholding Techniques and Edge Detection Techniques

---

## 1. Classical Filtering Techniques

The following filters were implemented using OpenCV:

### Mean Filter
Used to smooth an image by replacing each pixel with the average value of its neighboring pixels.

### Gaussian Filter
Used for image smoothing and noise reduction using a Gaussian kernel.

### Median Filter
Replaces each pixel with the median value of neighboring pixels. It is useful for removing salt-and-pepper noise.

### Bilateral Filter
Smooths the image while preserving important edges.

### Output Files

- mean_filter.jpg
- gaussian_filter.jpg
- median_filter.jpg
- bilateral_filter.jpg

---

## 2. Thresholding Techniques

The following thresholding methods were implemented:

### Binary Thresholding
Converts a grayscale image into a binary image using a fixed threshold.

### Inverse Binary Thresholding
Produces the inverse of binary thresholding.

### Adaptive Mean Thresholding
Calculates the threshold based on the local neighborhood of each pixel.

### Otsu's Thresholding
Automatically determines an appropriate threshold value from the image histogram.

### Output Files

- binary_threshold.jpg
- binary_inverse.jpg
- adaptive_mean.jpg
- otsu_threshold.jpg

---

## 3. Edge Detection Techniques

The following edge detection methods were implemented:

### Sobel Edge Detection
Detects edges by calculating image intensity gradients in horizontal and vertical directions.

### Prewitt Edge Detection
Uses horizontal and vertical convolution kernels to detect edges.

### Laplacian Edge Detection
Detects edges using the second derivative of the image.

### Canny Edge Detection
Detects edges using multiple stages including noise reduction, gradient calculation, non-maximum suppression and hysteresis thresholding.

### Output Files

- sobel_edges.jpg
- prewitt_edges.jpg
- laplacian_edges.jpg
- canny_edges.jpg

---

## Technologies Used

- Python
- OpenCV
- NumPy
- Matplotlib

---

## Project Structure

Image_Processing_Techniques/

├── images/

│   └── input.jpg

├── filtering/

│   ├── classical_filters.py

│   └── output/

│       ├── mean_filter.jpg

│       ├── gaussian_filter.jpg

│       ├── median_filter.jpg

│       └── bilateral_filter.jpg

├── thresholding/

│   ├── thresholding.py

│   └── output/

│       ├── binary_threshold.jpg

│       ├── binary_inverse.jpg

│       ├── adaptive_mean.jpg

│       └── otsu_threshold.jpg

├── edge_detection/

│   ├── edge_detection.py

│   └── output/

│       ├── sobel_edges.jpg

│       ├── prewitt_edges.jpg

│       ├── laplacian_edges.jpg

│       └── canny_edges.jpg

├── main.py

└── README.md

---

## Conclusion

Classical filtering, thresholding and edge detection techniques were successfully implemented using Python and OpenCV. The generated output images demonstrate the effect of different image processing techniques on the input image.