import imghdr
import cv2


def blur(image_path):
    try:
        image_type = imghdr.what(image_path)
        if image_type in ('jpg', 'jpeg', 'png'):
            image = cv2.imread(image_path, -1)
            image = cv2.GaussianBlur(image, (56, 55), cv2.BORDER_DEFAULT)
            cv2.imwrite('outputImage/blurredImg.jpg', image)
        else:
            print(f"Error: blur({image_path}) -> the file extension must be jpeg or png")

    except FileNotFoundError as e:
        print(f"Error: blur({image_path}) -> the file path is wrong or the file doesn't exist")

    except cv2.error as e:
        print(f"Error: blur({image_path}) -> the blur parameters must be odd numbers")
