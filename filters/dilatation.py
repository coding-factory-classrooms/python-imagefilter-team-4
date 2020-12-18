import cv2


# applique le filtre de dilatation
def dilate_image(image):
    from other.data import lib
    kernel = cv2.getStructuringElement(cv2.MORPH_DILATE, (lib['dilate_value'], lib['dilate_value']))
    dilatation = cv2.dilate(image, kernel, 6)
    return dilatation
