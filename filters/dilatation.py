import cv2


# applique le filtre de dilatation
def dilate_image(image):
    from configuration import cfg
    kernel = cv2.getStructuringElement(cv2.MORPH_DILATE, (cfg['dilate_value'], cfg['dilate_value']))
    dilatation = cv2.dilate(image, kernel, 6)
    return dilatation
