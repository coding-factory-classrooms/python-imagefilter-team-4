import cv2

# Applique le filtre flou
def blur_image(image):

    from other.data import lib
    blurImage = cv2.GaussianBlur(image, (lib['blur_value'], lib['blur_value']), 0)
    return blurImage
