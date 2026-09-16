import cv2
import matplotlib.pyplot as plt
import os
import numpy as np

# Get project root directory
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Input image path
image_path = os.path.join(project_root, "images", "input.jpg")

# Output folder
output_folder = os.path.join(project_root, "edge_detection", "output")

# Create output folder
os.makedirs(output_folder, exist_ok=True)

# Load image in grayscale
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Image not found!")
    print("Image path:", image_path)
    exit()

print("Grayscale image loaded successfully!")
print("Image shape:", image.shape)


# -----------------------------------
# 1. Sobel Edge Detection
# -----------------------------------

sobel_x = cv2.Sobel(
    image,
    cv2.CV_64F,
    1,
    0,
    ksize=3
)

sobel_y = cv2.Sobel(
    image,
    cv2.CV_64F,
    0,
    1,
    ksize=3
)

sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

sobel = cv2.addWeighted(
    sobel_x,
    0.5,
    sobel_y,
    0.5,
    0
)


# -----------------------------------
# 2. Prewitt Edge Detection
# -----------------------------------

prewitt_x_kernel = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
])

prewitt_y_kernel = np.array([
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
])

prewitt_x = cv2.filter2D(
    image,
    cv2.CV_64F,
    prewitt_x_kernel
)

prewitt_y = cv2.filter2D(
    image,
    cv2.CV_64F,
    prewitt_y_kernel
)

prewitt_x = cv2.convertScaleAbs(prewitt_x)
prewitt_y = cv2.convertScaleAbs(prewitt_y)

prewitt = cv2.addWeighted(
    prewitt_x,
    0.5,
    prewitt_y,
    0.5,
    0
)


# -----------------------------------
# 3. Laplacian Edge Detection
# -----------------------------------

laplacian = cv2.Laplacian(
    image,
    cv2.CV_64F
)

laplacian = cv2.convertScaleAbs(laplacian)


# -----------------------------------
# 4. Canny Edge Detection
# -----------------------------------

canny = cv2.Canny(
    image,
    100,
    200
)


# -----------------------------------
# Save Output Images
# -----------------------------------

cv2.imwrite(
    os.path.join(output_folder, "sobel_edges.jpg"),
    sobel
)

cv2.imwrite(
    os.path.join(output_folder, "prewitt_edges.jpg"),
    prewitt
)

cv2.imwrite(
    os.path.join(output_folder, "laplacian_edges.jpg"),
    laplacian
)

cv2.imwrite(
    os.path.join(output_folder, "canny_edges.jpg"),
    canny
)


print("All edge detection images saved successfully!")
print("Output folder:", output_folder)


# -----------------------------------
# Display Results
# -----------------------------------

plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.imshow(image, cmap="gray")
plt.title("Original Grayscale")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(sobel, cmap="gray")
plt.title("Sobel Edge Detection")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(prewitt, cmap="gray")
plt.title("Prewitt Edge Detection")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(laplacian, cmap="gray")
plt.title("Laplacian Edge Detection")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(canny, cmap="gray")
plt.title("Canny Edge Detection")
plt.axis("off")

plt.tight_layout()
plt.show()