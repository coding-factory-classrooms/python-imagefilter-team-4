import imghdr
import os  # Sert a parcourir les fichiers d'un dossier
import cv2
from filters import blackandwhite, blur, dilatation

# Chemin du dossier ou l'on veut appliquer les filtres
input_dir = 'image'
# Si le chemin du dossier est correct, éxécute le code normalement
try:
    files = os.listdir(input_dir)
    print(files)

    # Parcourt les fichiers du dossier
    for f in files:

        # Recupere les images
        file_path = f"{input_dir}/{f}"
        # Récupère le format de l'image
        image_type = imghdr.what(file_path)
        # Si le format d'image est incorrect, affiche une erreur
        if image_type not in ('jpg', 'jpeg', 'png'):
            print(f"Error: ({file_path}) -> the file extension must be jpeg or png")
        # Sinon, éxécute le code normalement
        else:
            image = cv2.imread(file_path)

            # Application filtre N&B
            image = blackandwhite.bandw_image(image)
            # Application filtre flou
            image = blur.blur_image(image)
            # Application filtre dilatation
            image = dilatation.dilate_image(image)
            # Enregistrement des fichiers dans un autre dossier
            cv2.imwrite(f"outputImage/{f}", image)

# Si le chemin du dossier est incorrect, affiche une erreur
except FileNotFoundError as e:
    print(f"Error: input_dir = '{input_dir}' -> the folder path is incorrect or the folder doesn't exist")
# Si le chemin du dossier n'est pas un dossier, affiche une erreur
except NotADirectoryError as e:
    print(f"Error: input_dir = '{input_dir}' -> path selected is not a folder")
# Si les paramètres de blur sont incorrects, affiche une erreur
except cv2.error as e:
    print(f"Error: blur_image() -> the blur parameters must be odd numbers and greater than 0")