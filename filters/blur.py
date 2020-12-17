import cv2


# Applique le filtre flou
def blur_image(image):
    blurImage = cv2.GaussianBlur(image, (55, 55), 0)
    return blurImage


