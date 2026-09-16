import cv2
import matplotlib.pyplot as plt
import os

# Get project root directory
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Input image path
image_path = os.path.join(project_root, "images", "input.jpg")

# Output folder
output_folder = os.path.join(project_root, "filtering", "output")

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Load original image
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")
    print("Image path:", image_path)
    exit()

# 1. Mean Filter
mean_filter = cv2.blur(image, (5, 5))

# 2. Gaussian Filter
gaussian_filter = cv2.GaussianBlur(image, (5, 5), 0)

# 3. Median Filter
median_filter = cv2.medianBlur(image, 5)

# 4. Bilateral Filter
bilateral_filter = cv2.bilateralFilter(image, 9, 75, 75)

# Save filtered images
cv2.imwrite(
    os.path.join(output_folder, "mean_filter.jpg"),
    mean_filter
)

cv2.imwrite(
    os.path.join(output_folder, "gaussian_filter.jpg"),
    gaussian_filter
)

cv2.imwrite(
    os.path.join(output_folder, "median_filter.jpg"),
    median_filter
)

cv2.imwrite(
    os.path.join(output_folder, "bilateral_filter.jpg"),
    bilateral_filter
)

print("All filtered images saved successfully!")
print("Output folder:", output_folder)

# Convert images to RGB for display
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
mean_rgb = cv2.cvtColor(mean_filter, cv2.COLOR_BGR2RGB)
gaussian_rgb = cv2.cvtColor(gaussian_filter, cv2.COLOR_BGR2RGB)
median_rgb = cv2.cvtColor(median_filter, cv2.COLOR_BGR2RGB)
bilateral_rgb = cv2.cvtColor(bilateral_filter, cv2.COLOR_BGR2RGB)

# Display results
plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(mean_rgb)
plt.title("Mean Filter")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(gaussian_rgb)
plt.title("Gaussian Filter")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(median_rgb)
plt.title("Median Filter")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(bilateral_rgb)
plt.title("Bilateral Filter")
plt.axis("off")

plt.tight_layout()
plt.show()