import cv2

#applique le filtre de dilatation
def dilate_image(image):
    kernel = cv2.getStructuringElement(cv2.MORPH_DILATE, (10, 10))
    dilatation = cv2.dilate(image, kernel, 6)

    return dilatation
