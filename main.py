import imghdr
import sys
import os  # Sert a parcourir les fichiers d'un dossier
import cv2
from other import logger, CLI
from other.data import lib

args = sys.argv


# Chemin du dossier ou l'on veut appliquer les filtre


# Si le chemin du dossier est correct, éxécute le code normalement
try:
    CLI.default_args(args)
    CLI.default_cfg()
    input_dir = lib['input_dir']
    output_dir = lib['output_dir']

    files = os.listdir(input_dir)

    # Parcourt les fichiers du dossier
    for f in files:

        # Récupère les images
        file_path = f"{input_dir}/{f}"
        # Récupère le format de l'image
        image_type = imghdr.what(file_path)
        image = cv2.imread(file_path)

        # Si le format d'image est incorrect, affiche une erreur
        if image_type not in ('jpg', 'jpeg', 'png'):
            print(f"Error: ({file_path}) -> the file extension must be jpeg or png")
            logger.log(f"Error: ({file_path}) -> the file extension must be jpeg or png")
        # Sinon, éxécute le code normalement
        else:
            # Execute le programme avec paramètres si il détecte au moins un paramètre de lancement

            if len(args) > 1:
                CLI.filters_args(args)

            # Execute le programme normalement si il n'y a pas de paramètres de lancement
            else:
                # Apllication des filtres après runs
                # Application filtre N&B
                image = lib['bandw'](image)
                # Application filtre flou
                image = lib['blur'](image)
                # Application filtre dilatation
                image = lib['dilate'](image)

                # Enregistrement des fichiers dans un autre dossier
                cv2.imwrite(f"{output_dir}/{f}", image)


# Si le chemin du dossier est incorrect, affiche une erreur
except FileNotFoundError as e:
    print(f"Error: input_dir = '{lib['input_dir']}' -> the folder path is incorrect or the folder doesn't exist")
    logger.log(f"Error: input_dir = '{lib['input_dir']}' -> the folder path is incorrect or the folder doesn't exist")
# Si le chemin du dossier n'est pas un dossier, affiche une erreur
except NotADirectoryError as e:
    print(f"Error: input_dir = '{lib['input_dir']}' -> path selected is not a folder")
    logger.log(f"Error: input_dir = '{lib['input_dir']}' -> path selected is not a folder")
# Si les paramètres de blur sont incorrects, affiche une erreur
except cv2.error as e:
    print(f"Error: blur_image() -> the blur parameters must be odd numbers and greater than 0")
    logger.log(f"Error: blur_image() -> the blur parameters must be odd numbers and greater than 0")
except IndexError as e:
    print(
        f"Error: you must specify a correct folder path with launch parameters -i and -o (-i input_path or -o "
        f"output_path)")
    logger.log(
        f"Error: you must specify a correct folder path with launch parameters -i and -o (-i input_path or -o "
        f"output_path)")
