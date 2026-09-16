import cv2
import matplotlib.pyplot as plt

# Load image
image = cv2.imread("images/input.jpg")

# Check whether image is loaded
if image is None:
    print("Error: Image not found!")
else:
    print("Image loaded successfully!")
    print("Image shape:", image.shape)

    # Convert BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Display image
    plt.imshow(image_rgb)
    plt.title("Original Image")
    plt.axis("off")
    plt.show()