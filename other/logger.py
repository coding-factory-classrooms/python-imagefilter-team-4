from other.data import lib


def log(msg):
    """
    this function allows to write in the file imagefilter.log
    :param msg: allows you to add an operation to the file
    :return:displays the operation in the imagefilter.log file
    """
    with open(lib['log_file'], 'a') as f:
        f.write(msg + '\n')
