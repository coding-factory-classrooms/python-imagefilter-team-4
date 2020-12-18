import cv2

from other import logger
from other.data import lib
from filters import filterzeteam


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
    # Changes the image input path if the -i launch parameter is present with another path
    for i in range(len(args)):
        if args[i] == "-i":
            lib['input_dir'] = args[i + 1]
        # Changes the output path of the images if the launch parameter -o is present with another path
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
    # Analyze each launch parameter
    if "--filters" in args:
        for i in range(len(args)):

            # If a filter parameter is present, enter the loop
            if args[i] == "--filters":
                # Assigns the value after the parameter in a variable
                filter_arg = args[i + 1]
                # Separates the value into multiple objects according to the character of the splitter
                arg_split = filter_arg.split('|')

                # Analyzes each splitter object
                for k in arg_split:
                    # Separates the filter type and filter value of each object
                    filter_split = k.split(':')

                    # Assigns the filter type and value to two variables
                    filter_type = filter_split[0]

                    # Black and white filter application
                    # --filters --blackandwhite = --filters black --filters blackandwhite|blur
                    if filter_type == "grayscale":
                        image = lib['bandw'](image)
                        logger.log("The black and white filter has been applied")
                    # Blur filter application
                    elif filter_type == "blur":
                        lib['blur_value'] = int(filter_split[1])
                        image = lib['blur'](image)
                        logger.log("The blur filter has been applied")
                    # Dilatation filter application
                    elif filter_type == "dilate":
                        lib['dilate_value'] = int(filter_split[1])
                        image = lib['dilate'](image)
                        logger.log("The dilatation filter has been applied")

                    image = filterzeteam.filter_ze_team(image)

    else:
        # Applying filters after runs
        # Black and white filter application
        image = lib['bandw'](image)
        # Blur filter application
        image = lib['blur'](image)
        # Dilatation filter application
        image = lib['dilate'](image)

    image = filterzeteam.filter_ze_team(image)
    # Saving files to another folder
    cv2.imwrite(f"{output_dir}/{f}", image)
    # Displays the result in another window and waits for a keyboard input from the user
    cv2.imshow("Output", image)
    cv2.waitKey(0)
