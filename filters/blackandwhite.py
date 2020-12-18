import cv2


# Applique le filtre N&B
def bandw_image(image):
    """
       allows you to apply a filter B&W to an image
       :param image: apply the filter to the images
       :return: the images with the filter
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray
