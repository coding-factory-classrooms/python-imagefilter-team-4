import imghdr
import sys
import os  # Sert a parcourir les fichiers d'un dossier
import cv2
import logger
from filters import blackandwhite, blur, dilatation

args = sys.argv
print(args)

# Chemin du dossier ou l'on veut appliquer les filtres
input_dir = 'image'
output_dir = 'outputImage'

# Si le chemin du dossier est correct, éxécute le code normalement
try:
    # Modifie le chemin d'input des images si le paramètre de lancement -i est présent avec un autre chemin
    for i in range(len(args)):
        if args[i] == "-i":
            input_dir = args[i + 1]
        # Modifie le chemin d'output des images si le paramètre de lancement -o est présent avec un autre chemin
        elif args[i] == "-o":
            output_dir = args[i + 1]

    files = os.listdir(input_dir)
    print(files)

    # Parcourt les fichiers du dossier
    for f in files:

        # Récupère les images
        file_path = f"{input_dir}/{f}"
        # Récupère le format de l'image
        image_type = imghdr.what(file_path)
        image = cv2.imread(file_path)

        # Si le format d'image est incorrect, affiche une erreur
        if image_type not in ('jpg', 'jpeg', 'png'):
            logger.log(f"Error: ({file_path}) -> the file extension must be jpeg or png")
        # Sinon, éxécute le code normalement
        else:
            # Execute le programme avec paramètres si il détecte au moins un paramètre de lancement
            if len(args) > 1:
                # Choix du filtre en utilisant les parametres
                for i in range(len(args)):
                    # Application filtre N&B
                    if args[i] == "--blackandwhite":
                        image = blackandwhite.bandw_image(image)
                        logger.log("le filtre noir et blanc a été appliqué")
                    # Application filtre flou
                    elif args[i] == "--blur":
                        image = blur.blur_image(image)
                        logger.log("le filtre flou a été appliqué")
                    # Application filtre dilatation
                    elif args[i] == "--dilatation":
                        image = dilatation.dilate_image(image)
                        logger.log("le filtre de dilatation a été appliqué")

                # Enregistrement des fichiers dans un autre dossier
                cv2.imwrite(f"{output_dir}/{f}", image)
                # Affiche le résultat dans une autre fenêtre et attend un input clavier de l'utilisateur
                cv2.imshow("Output", image)
                cv2.waitKey(0)

            # Execute le programme normalement si il n'y a pas de paramètres de lancement
            else:
                # Apllication des filtres après runs
                # Application filtre N&B
                image = blackandwhite.bandw_image(image)
                # Application filtre flou
                image = blur.blur_image(image)
                # Application filtre dilatation
                image = dilatation.dilate_image(image)

                # Enregistrement des fichiers dans un autre dossier
                cv2.imwrite(f"{output_dir}/{f}", image)

# Si le chemin du dossier est incorrect, affiche une erreur
except FileNotFoundError as e:
    logger.log(f"Error: input_dir = '{input_dir}' -> the folder path is incorrect or the folder doesn't exist")
# Si le chemin du dossier n'est pas un dossier, affiche une erreur
except NotADirectoryError as e:
    logger.log(f"Error: input_dir = '{input_dir}' -> path selected is not a folder")
# Si les paramètres de blur sont incorrects, affiche une erreur
except cv2.error as e:
    logger.log(f"Error: blur_image() -> the blur parameters must be odd numbers and greater than 0")
except IndexError as e:
    logger.log(f"Error: you must specify a correct folder path with launch parameters -i and -o (-i input_path or -o output_path)")