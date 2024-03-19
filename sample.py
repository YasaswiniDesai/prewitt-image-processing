from PIL import Image

# Open the image
img = Image.open("girl.png")

# Convert the image to grayscale
img_gray = img.convert("L")

# Get the dimensions of the image
width, height = img_gray.size

# Load pixel data
pixels = img_gray.load()

# Define the vertical and horizontal edge detectors
ver = [[-1, 0, 1],
       [-1, 0, 1],
       [-1, 0, 1]]

hor = [[-1, -1, -1],
       [0, 0, 0],
       [1, 1, 1]]

# Function to clamp pixel value between 0 and 255
def clamp(value):
    return max(0, min(value, 255))

# Iterate over each pixel in the image (except the border pixels)
for y in range(1, height - 1):
    for x in range(1, width - 1):
        # Apply the vertical and horizontal edge detectors
        ver_sum = sum(ver[i][j] * pixels[x - 1 + i, y - 1 + j] for i in range(3) for j in range(3))
        hor_sum = sum(hor[i][j] * pixels[x - 1 + i, y - 1 + j] for i in range(3) for j in range(3))

        # Calculate magnitude of the edge
        edge_mag = int((ver_sum ** 2 + hor_sum ** 2) ** 0.5)

        # Update the pixel value
        pixels[x, y] = clamp(edge_mag)

# Display the resulting image
img_gray.show()
