import imghdr
import sys
import os  # Sert a parcourir les fichiers d'un dossier
import cv2
import logger
from configuration import cfg

args = sys.argv
# print(args)

# Chemin du dossier ou l'on veut appliquer les filtre
input_dir = cfg['input_dir']
output_dir = cfg['output_dir']

# Si le chemin du dossier est correct, éxécute le code normalement
try:
    # Modifie le chemin d'input des images si le paramètre de lancement -i est présent avec un autre chemin
    for i in range(len(args)):
        if args[i] == "-i":
            input_dir = args[i + 1]
        # Modifie le chemin d'output des images si le paramètre de lancement -o est présent avec un autre chemin
        elif args[i] == "-o":
            output_dir = args[i + 1]
        elif args[i] == "-h":
            print(cfg['help'])

    files = os.listdir(input_dir)
    # print(files)

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
                # Analyse chaque paramètre de lancement
                for i in range(len(args)):

                    # Si un paramètre filtre est présent, rentre dans la boucle
                    if args[i] == "--filters":
                        # Attribue la valeur après le paramètre dans une variabke
                        filter_arg = args[i+1]
                        # Sépare la valeur en plusieurs objets selon le caractère du splitter
                        arg_split = filter_arg.split('|')
                        print(arg_split)

                        # Analyse chaque objet du splitter
                        for k in arg_split:
                            # Sépare le type de filtre et la valeur du filtre de chaque objet
                            filter_split = k.split(':')
                            print(filter_split)
                            # Attribue le type et la valeur du filtre a deux variables
                            filter_type = filter_split[0]

                            # Application filtre N&B
                            # --filters --blackandwhite = --filters black --filters blackandwhite|blur
                            if filter_type == "grayscale":
                                image = cfg['bandw'](image)
                                logger.log("le filtre noir et blanc a été appliqué")
                            # Application filtre flou
                            elif filter_type == "blur":
                                cfg['blur_value'] = int(filter_split[1])
                                image = cfg['blur'](image)
                                logger.log("le filtre flou a été appliqué")
                            # Application filtre dilatation
                            elif filter_type == "dilate":
                                cfg['dilate_value'] = int(filter_split[1])
                                image = cfg['dilate'](image)
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
                image = cfg['bandw'](image)
                # Application filtre flou
                image = cfg['blur'](image)
                # Application filtre dilatation
                image = cfg['dilate'](image)

                # Enregistrement des fichiers dans un autre dossier
                cv2.imwrite(f"{output_dir}/{f}", image)

# Si le chemin du dossier est incorrect, affiche une erreur
except FileNotFoundError as e:
    print(f"Error: input_dir = '{input_dir}' -> the folder path is incorrect or the folder doesn't exist")
    logger.log(f"Error: input_dir = '{input_dir}' -> the folder path is incorrect or the folder doesn't exist")
# Si le chemin du dossier n'est pas un dossier, affiche une erreur
except NotADirectoryError as e:
    print(f"Error: input_dir = '{input_dir}' -> path selected is not a folder")
    logger.log(f"Error: input_dir = '{input_dir}' -> path selected is not a folder")
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
