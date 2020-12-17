import sys
import cv2
import os
from filters import blackandwhite, blur

input_dir = 'image'
files = os.listdir(input_dir)
for f in files:

    # Recupere les images
    file_path = f"{input_dir}/{f}"
    image = cv2.imread(file_path)

    args = sys.argv
    print(args)
    for args in sys.argv:
        if args == "--blackandwhite":
            image = blackandwhite.bandw_image(image)
            cv2.imshow("Gray", image)
            cv2.waitKey(0)
        elif args == "--blur":
            image = blur.blur_image(image)
            cv2.imshow("Blur", image)
            cv2.waitKey(0)
