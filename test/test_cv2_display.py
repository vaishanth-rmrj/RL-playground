import cv2
import numpy as np

# Create a red image (BGR format, 255 in the red channel)
red_image = np.zeros((500, 500, 3), dtype=np.uint8)
red_image[:] = (0, 0, 255)  # BGR: Blue=0, Green=0, Red=255

# Display the image
cv2.imshow("Red Image", red_image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
