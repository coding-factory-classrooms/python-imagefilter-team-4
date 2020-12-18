import cv2

from other import logger
from other.data import lib


def default_cfg():
    """
    Looks for the --config-file argument in main and implements all the variables from the .ini file.
    """
    from main import args
    if '--config-file' in args:
        import configparser

        i = args.index('--config-file')
        config_file = args[i + 1]
        parser = configparser.SafeConfigParser()
        parser.read(config_file)
        args.clear()
        lib['input_dir'] = parser.get('Default', 'input_dir')
        lib['output_dir'] = parser.get('Default', 'output_dir')
        lib['log_file'] = parser.get('Default', 'log_file')
        parse_filters = parser.get('Default', 'filters')
        args.append("--filters")
        args.append(parse_filters)


def override_cfg():
    """
    Looks for the --config-file argument in main and implements all the variables from the .ini file.
    """
    from main import args
    if '--config-file' in args:
        import configparser

        i = args.index('--config-file')
        config_file = args[i + 1]
        parser = configparser.SafeConfigParser()
        parser.read(config_file)

        lib['input_dir'] = parser.get('Default', 'input_dir')
        lib['output_dir'] = parser.get('Default', 'output_dir')
        lib['log_file'] = parser.get('Default', 'log_file')
        parse_filters = parser.get('Default', 'filters')
        args.append("--filters")
        args.append(parse_filters)


def default_args(args):
    """
    Looks for arguments in main and uses it for different actions like change input/output file
    :param args: the arguments list put in the main
    """
    # Modifie le chemin d'input des images si le paramètre de lancement -i est présent avec un autre chemin
    for i in range(len(args)):
        if args[i] == "-i":
            lib['input_dir'] = args[i + 1]
        # Modifie le chemin d'output des images si le paramètre de lancement -o est présent avec un autre chemin
        elif args[i] == "-o":
            lib['output_dir'] = args[i + 1]
        elif args[i] == "-h":
            print(lib['help'])
        elif args[i] == '--log-file':
            lib['log_file'] = f"{args[i + 1]}.log"


def filters_args(args):
    """
    Looks for --filters argument in main and apply the filters and parameters that follows to the images.
    If no --filters argument is present, apply default filters with default values.
    :param args: the arguments list put in the main
    """
    from main import output_dir, image, f
    # Analyse chaque paramètre de lancement
    if "--filters" in args:
        for i in range(len(args)):

            # Si un paramètre filtre est présent, rentre dans la boucle
            if args[i] == "--filters":
                # Attribue la valeur après le paramètre dans une variabke
                filter_arg = args[i + 1]
                # Sépare la valeur en plusieurs objets selon le caractère du splitter
                arg_split = filter_arg.split('|')

                # Analyse chaque objet du splitter
                for k in arg_split:
                    # Sépare le type de filtre et la valeur du filtre de chaque objet
                    filter_split = k.split(':')

                    # Attribue le type et la valeur du filtre a deux variables
                    filter_type = filter_split[0]

                    # Application filtre N&B
                    # --filters --blackandwhite = --filters black --filters blackandwhite|blur
                    if filter_type == "grayscale":
                        image = lib['bandw'](image)
                        logger.log("le filtre noir et blanc a été appliqué")
                    # Application filtre flou
                    elif filter_type == "blur":
                        lib['blur_value'] = int(filter_split[1])
                        image = lib['blur'](image)
                        logger.log("le filtre flou a été appliqué")
                    # Application filtre dilatation
                    elif filter_type == "dilate":
                        lib['dilate_value'] = int(filter_split[1])
                        image = lib['dilate'](image)
                        logger.log("le filtre de dilatation a été appliqué")

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
    # Affiche le résultat dans une autre fenêtre et attend un input clavier de l'utilisateur
    cv2.imshow("Output", image)
    cv2.waitKey(0)
