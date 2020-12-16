import cv2


def convertImage():
    image = cv2.imread('image/humour.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow('image/humour.jpg', image)
    cv2.imshow('Gray humour', gray)


def saveImage(gray):
    convertImage()
    cv2.imwrite('outputImage/GrayHumour.jpg', gray)
