import os # Sert a parcourir les fichiers d'un dossier
import cv2
from filters import blackandwhite, blur

# Check les fichiers dans le dossier
input_dir = 'image'
files = os.listdir(input_dir)
print(files)

# Parcourt les fichiers du dossier
for f in files:

    # Recupere les images
    file_path = f"{input_dir}/{f}"
    image = cv2.imread(file_path)

    # Application filtre N&B
    image = blackandwhite.bandw_image(image)
    # Application filtre flou
    image = blur.blur_image(image)
    # Application filtre dilatation


    # Enregistrement des fichiers dans un autre dossier
    cv2.imwrite(f"outputImage/{f}", image)