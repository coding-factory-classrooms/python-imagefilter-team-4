import imghdr
import sys
import os  # Used to browse files in a folder
import cv2
from other import logger, CLI
from other.data import lib

args = sys.argv


# Folder path where you want to apply the filters


# If the folder path is correct, run the code normally
try:
    CLI.default_args(args)
    CLI.default_cfg()
    input_dir = lib['input_dir']
    output_dir = lib['output_dir']

    files = os.listdir(input_dir)

    # Browse the files in the folder
    for f in files:

        # Recovers images
        file_path = f"{input_dir}/{f}"
        # Recovers the format of the image
        image_type = imghdr.what(file_path)
        image = cv2.imread(file_path)

        # If the image format is incorrect, displays an error
        if image_type not in ('jpg', 'jpeg', 'png'):
            print(f"Error: ({file_path}) -> the file extension must be jpeg or png")
            logger.log(f"Error: ({file_path}) -> the file extension must be jpeg or png")
        # Otherwise, run the code normally
        else:
            # Execute the program with parameters if it detects at least one launch parameter

            if len(args) > 1:
                CLI.filters_args(args)

            # Execute the program normally if there are no launch parameters
            else:
                # Applying filters after runs
                # Black and white filter application
                image = lib['bandw'](image)
                # Blur filter application
                image = lib['blur'](image)
                # Dilatation filter application
                image = lib['dilate'](image)

                # Saving files to another folder
                cv2.imwrite(f"{output_dir}/{f}", image)


# If the folder path is incorrect, displays an error
except FileNotFoundError as e:
    print(f"Error: input_dir = '{lib['input_dir']}' -> the folder path is incorrect or the folder doesn't exist")
    logger.log(f"Error: input_dir = '{lib['input_dir']}' -> the folder path is incorrect or the folder doesn't exist")
# If the folder path is not a folder, displays an error
except NotADirectoryError as e:
    print(f"Error: input_dir = '{lib['input_dir']}' -> path selected is not a folder")
    logger.log(f"Error: input_dir = '{lib['input_dir']}' -> path selected is not a folder")
# If the blur settings are incorrect, displays an error
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
