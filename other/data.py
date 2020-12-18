from filters import blackandwhite, blur, dilatation

lib = {
    # Chemin du dossier ou l'on veut appliquer les filtres
    'input_dir': 'image',
    'output_dir': 'outputImage',
    'blur_value': 55,
    'dilate_value': 10,
    'bandw': blackandwhite.bandw_image,
    'blur': blur.blur_image,
    'dilate': dilatation.dilate_image,
    'log_file': 'imagefilter.log',
    'help': '-h --------> display help\n'
            '-i ---> -i <input directory>\n'
            '-o ---> -i <output directory>\n'
}
