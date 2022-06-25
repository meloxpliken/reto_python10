import os
from os.path import exists
from pathlib import Path
import toml
import shutil
import mimetypes


HOME = os.path.expanduser('~')
USER_DIRS = f"{HOME}/.config/user-dirs.dirs"
USER_DIRS_DICT = {}
MIMETYPES = {'.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp', '.png': 'image/png', '.txt': 'text/plain'}
TOML_DICT = {'directorios': {
                    '1': {'in': '/home/meloxpliken/pruebas/dir1-in1/', 'out': '/home/meloxpliken/pruebas/dir1-out1/', 'actions': ['copy', 'move'], 'filter': '*.png'}, 
                    '2': {'in': '/home/meloxpliken/pruebas/dir2-in2/', 'out': '/home/meloxpliken/pruebas/dir2-out2/', 'actions': ['move'], 'filter': '*.jpeg'}, 
                    '3': {'in': '/home/meloxpliken/pruebas/dir3-in3/', 'out': '/home/meloxpliken/pruebas/dir3-out3/', 'actions': ['copy', 'none'], 'filter': '*.txt'}}}

mimetypes.init()


class Configurator():


    def __init__(self, TOML_DIR, TOML_FILE):
        self.TOML_DIR = TOML_DIR
        self.TOML_FILE = TOML_FILE
        self.check_toml()


    def check_toml(self):
        '''
        FUNCIÓN QUE COMPRUEBA EXISTENCIA FICHERO TOML
        - SI NO EXISTE EN DIRECTORIO LO CREA
        - SI NO EXISTE EL FICHERO LO CREA Y LO RELLENA CON EL DIRECTORIO DE USUARIO
        - SI EXISTE CARGA LAS ASIGNACIONES A UN DICCIONARIO
        '''
        os.makedirs(self.TOML_DIR, exist_ok=True)

        if not exists(self.TOML_FILE):
            self.find_users_dirs()
#            TOML_DICT["directorio"] = USER_DIRS_DICT["XDG_DOWNLOAD_DIR"]
            with open(self.TOML_FILE, "w", encoding="utf-8") as fp:
                toml.dump(TOML_DICT, fp)

        for dir in TOML_DICT['directorios'].values():
#            print('*', dir, '*')
            #print(f"{dir['in']} -- {dir['out']}")
            os.makedirs(dir['in'],  exist_ok=True)
            os.makedirs(dir['out'], exist_ok=True)


    def find_users_dirs(self):
        '''
        FUNCIÓN QUE CREA UN DICT CON LOS DIRECTORIOS DE USUARIO
        '''
        if exists(USER_DIRS):
            with open(USER_DIRS, "rt", encoding="utf-8") as config_dirs:
                content = config_dirs.readlines()
            for line in content:
                if line.startswith("XDG"):
                    item_list = line.strip("\n").split("=")
                    USER_DIRS_DICT[item_list[0]] = item_list[1].replace("$HOME", HOME).replace('"', "")
#            for clave, valor in USER_DIRS_DICT.items():
#                print(clave, '--', valor)


    def read(self):
        #self.TOML_DICT = toml.load(self.TOML_FILE)
#        datos = toml.load(self.TOML_FILE)
        print(f"\n{toml.dumps(datos)}")
#        print(datos)
        return toml.load(self.TOML_FILE)


    def do_action(self):
        data = self.read()
        for dir in data['directorios'].values():    
#            print(f"dir_in: {dir['in']}; dir_out: {dir['out']}")
            if 'in' in dir and 'out' in dir and 'actions' in dir:
                print('****' , dir)
                dir_in  = Path(dir['in'])
                dir_out = Path(dir['out'])
                filtro  = dir['filter']
                actions = dir['actions']
#               print(MIMETYPES[filtro[1:]])
#               print(f"dir_in: {dir_in}; dir_out: {dir_out}; filtro: {filtro}")
                if os.path.isdir(dir_in) and os.path.isdir(dir_out):
                    for item in dir_in.glob(filtro):
                        if item.is_file():
                            print(f"archivo: {item}")          
                            for action in actions: 
                                print(f"ACCIÓN: {action}") 
                                dest = dir_out / item.name
                                if action == 'copy':    
                                    print(f"     COPIO -> {dest}")
                                    shutil.copy(item, dest)
                                    #print('     COPIO ->' , os.path.join(dir['in'], file), dir['out'])
                                elif action == 'move':
                                    print(f"     MUEVO -> {dest}")
                                    shutil.move(item, dest)
                                    #print('     MUEVO ->' , os.path.join(dir['in'], file), dir['out'])    def do_action(self):           


    def do_action2(self):
        data = self.read()
        for dir in data['directorios'].values():    
#            print(f"dir_in: {dir['in']}; dir_out: {dir['out']}")
            print('****' , dir)
            dir_in  = dir['in']
            dir_out = dir['out']
            filtro  = dir['filter']
#            print(MIMETYPES[filtro[1:]])
#            print(f"dir_in: {dir_in}; dir_out: {dir_out}; filtro: {filtro}")
            if 'in' in dir and 'out' in dir and 'actions' in dir:
                if os.path.isdir(dir_in) and os.path.isdir(dir_out):
                    for action in dir['actions']:  
                        print(f"     --> {action} - {filtro} - {MIMETYPES[filtro[1:]]}")                  
                        #print(f"####{file} -- {mimetypes.guess_type(os.path.join(dir['in'], file))[0]}")
                        for file in [file for file in os.listdir(dir_in)
                                        if os.path.isfile(os.path.join(dir_in, file)) and
                                        mimetypes.guess_type(os.path.join(dir_in, file))[0] in MIMETYPES[filtro[1:]]]:
                            if action == 'copy':    
                                shutil.copy(os.path.join(dir_in, file), dir_out)
                                print(f"     COPIO -> {file} -- {mimetypes.guess_type(os.path.join(dir_in, file))[0]}")
                                #print('     COPIO ->' , os.path.join(dir['in'], file), dir['out'])
                            elif action == 'move':
                                if not(os.path.exists(os.path.join(dir_out, file))):
                                    shutil.move(os.path.join(dir_in, file), dir_out)
                                    print(f"     MUEVO -> {file} -- {mimetypes.guess_type(os.path.join(dir_in, file))[0]}")
                                    #print('     MUEVO ->' , os.path.join(dir['in'], file), dir['out'])
                                    