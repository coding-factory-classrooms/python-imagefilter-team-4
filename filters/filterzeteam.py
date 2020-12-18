import cv2

# font
font = cv2.FONT_HERSHEY_SIMPLEX
# org
org = (50, 50)
# fontScale
fontScale = 1
# Blue color in BGR
color = (0, 0, 255)
# Line thickness of 2 px
thickness = 2

def filter_ze_team(image):
    text = "Maxime\nAlexis\nJohanna"
    y0, dy = 100, 50
    for i, line in enumerate(text.split('\n')):
        y = y0 + i * dy
        cv2.putText(image, line, (50, y), font, fontScale, color, thickness, cv2.LINE_AA)
    # Using cv2.putText() method
    #image = cv2.putText(image, "Maxime", org, font,fontScale, color, thickness, cv2.LINE_AA)
    return image

