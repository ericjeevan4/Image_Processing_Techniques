import cv2
import matplotlib.pyplot as plt
import os

# Get project root directory
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Input image path
image_path = os.path.join(project_root, "images", "input.jpg")

# Output folder
output_folder = os.path.join(project_root, "thresholding", "output")

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
# 1. Binary Thresholding
# -----------------------------------

_, binary = cv2.threshold(
    image,
    127,
    255,
    cv2.THRESH_BINARY
)


# -----------------------------------
# 2. Inverse Binary Thresholding
# -----------------------------------

_, binary_inverse = cv2.threshold(
    image,
    127,
    255,
    cv2.THRESH_BINARY_INV
)


# -----------------------------------
# 3. Adaptive Mean Thresholding
# -----------------------------------

adaptive_mean = cv2.adaptiveThreshold(
    image,
    255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)


# -----------------------------------
# 4. Otsu's Thresholding
# -----------------------------------

otsu_threshold, otsu = cv2.threshold(
    image,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)


# -----------------------------------
# Save Output Images
# -----------------------------------

cv2.imwrite(
    os.path.join(output_folder, "binary_threshold.jpg"),
    binary
)

cv2.imwrite(
    os.path.join(output_folder, "binary_inverse.jpg"),
    binary_inverse
)

cv2.imwrite(
    os.path.join(output_folder, "adaptive_mean.jpg"),
    adaptive_mean
)

cv2.imwrite(
    os.path.join(output_folder, "otsu_threshold.jpg"),
    otsu
)


print("All thresholding images saved successfully!")
print("Otsu threshold value:", otsu_threshold)
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
plt.imshow(binary, cmap="gray")
plt.title("Binary Threshold")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(binary_inverse, cmap="gray")
plt.title("Inverse Binary")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(adaptive_mean, cmap="gray")
plt.title("Adaptive Mean")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(otsu, cmap="gray")
plt.title("Otsu Threshold")
plt.axis("off")

plt.tight_layout()
plt.show()