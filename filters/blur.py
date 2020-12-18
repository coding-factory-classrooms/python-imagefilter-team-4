import cv2


# Applique le filtre flou
def blur_image(image):
    """
    Apply a blur filter on the image with the parameter available in library.
    :param image: An image from the input folder.
    :return: The image with the blur filter applied.
    """
    from other.data import lib
    blurImage = cv2.GaussianBlur(image, (lib['blur_value'], lib['blur_value']), 0)
    return blurImage
