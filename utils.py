import os
import mimetypes

mimetypes.init()


def list_dir(user_path, filetype):
    '''
    FUNCIÓN QUE LISTA SÓLO FICHEROS EN DIRECTORIOS
    '''
    if os.path.isdir(user_path):
        for file in [file for file in os.listdir(user_path)
                     if os.path.isfile(os.path.join(user_path, file))]:
                    #and mimetypes.guess_type(os.path.join(user_path, file))[0] in [filetype]]:
            print(file)