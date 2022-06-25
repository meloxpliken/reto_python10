import os
from configurator import Configurator
from utils import *


HOME = os.path.expanduser('~')
TOML_DIR  = f"{HOME}/.config/diogenes"
TOML_FILE = f"{HOME}/.config/diogenes/diogenes.conf"
FILE_TYPE = 'image/jpeg'


def main():
    configurator = Configurator(TOML_DIR, TOML_FILE)
    data = configurator.read()

    for dir in data['directorios'].values():
        print(f"=== {dir['in']} ===")
        list_dir(dir['in'], FILE_TYPE)

#        if dir['action'] == 'copy':
#            copiar(dir['in'], dir['out'])
#        elif dir['action'] == 'move':
#            mover(dir['in'], dir['out'])
#        else:
#            continue

    configurator.do_action2()


if __name__ == '__main__':  # es el módulo que se ejecuta como principal
    main()
