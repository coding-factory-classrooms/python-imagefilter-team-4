import cv2


# applique le filtre de dilatation
def dilate_image(image):
    """
    allows you to apply a dilatation filter to an image
    :param image: apply the filter to the images
    :return: the images with the filter
    """
    from other.data import lib
    kernel = cv2.getStructuringElement(cv2.MORPH_DILATE, (lib['dilate_value'], lib['dilate_value']))
    dilatation = cv2.dilate(image, kernel, 6)
    return dilatation
