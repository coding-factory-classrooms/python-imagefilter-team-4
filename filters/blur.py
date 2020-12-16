import cv2


def blur():

    image = cv2.imread('image/meme.jpg', -1)
    image = cv2.GaussianBlur(image, (51, 51), cv2.BORDER_DEFAULT)

    cv2.imwrite('outputImage/blurredmeme.jpg', image)



