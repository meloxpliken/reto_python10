import os
from pathlib import Path
from PIL import Image
import pilgram
#from os.path import exists


HOME = os.path.expanduser('~')
FILTERS = [
    "_1977", "aden", "brannan", "brooklyn", "clarendon", "earlybird",
    "gingham", "hudson", "inkwell", "kelvin", "lark", "lofi", "maven",
    "mayfair", "moon", "nashville", "perpetua", "reyes", "rise",
    "slumber", "stinson", "toaster", "valencia", "walden", "willow", "xpro2"]


class InstagramImage:

    def __init__(self, filein, fileout, args={}):
        self._filein = filein
        self._fileout = fileout
        self._args = args
        print(args)


    def check(self):
        print("entro a checkearrrrr")
        if not self._filein.exists() or not self._filein.is_file(): 
            return False
        if not self._fileout.parent.exists() or \
                not self._fileout.parent.is_dir(): 
            return False
        if "filter" not in self._args.keys() or \
                self._args['filter'] not in FILTERS:
            return False

        return True


    def execute(self):  
        image = Image.open(self._filein)
        filter_name = self._args['filter']
        print(f"{self._filein} \n{filter_name} \n{self._fileout}")
        filter = getattr(pilgram, filter_name)
        filter(image).save(self._fileout)


def main():
    filter_name = "lofi"
    filein = Path(f"{HOME}/pruebas/12.jpg")
    fileout = Path(f"{HOME}/pruebas/12_{filter_name}.jpg")
    if action.check():
        action = InstagramImage(filein, fileout, {"filter": filter_name})
        action.execute()


if __name__ == '__main__':  # es el módulo que se ejecuta como principal
    main()
