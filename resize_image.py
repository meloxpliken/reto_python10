from PIL import Image
from pathlib import Path
import os
from os.path import exists


HOME = os.path.expanduser('~')



class ResizeImage():

    def __init__(self, filein, fileout, args):
        self.__filein = filein
        self.__fileout = fileout
        self.__args = args


    def check(self):
        print("entro a checkear")
        if not exists(self.__filein) or not self.__filein.is_file(): 
            print(f"self.__filein: {self.__filein}")
            return False
        if "width" not in self.__args or "height" not in self.__args  :
            print(f"self.__args: {self.__args}")
            return False

        return True


    def execute(self):	
        size=(self.__args["width"], self.__args["height"])
        image = Image.open(self.__filein)
        image = image.resize(size)
        image.save(self.__fileout)
        image.show()


def main():
    filein = Path(f"{HOME}/pruebas/Baby-Yoda.png")
    fileout = Path(f"{HOME}/pruebas/salida.png")
    args = {"width": 200, "height": 200}
    resize_image = ResizeImage(filein, fileout, args)
    if resize_image.check():
        resize_image.execute()


if __name__ == '__main__':  # es el módulo que se ejecuta como principal
    main()