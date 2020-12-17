import cv2


# Applique le filtre flou
def blur_image(image):
    from configuration import cfg
    blurImage = cv2.GaussianBlur(image, (cfg['blur_value'], cfg['blur_value']), 0)
    return blurImage
