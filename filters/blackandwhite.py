import cv2

# Applique le filtre N&B
def bandw_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray
