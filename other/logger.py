from other.data import lib


def log(msg):
    with open(lib['log_file'], 'a') as f:
        f.write(msg + '\n')
