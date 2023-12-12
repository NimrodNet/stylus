import shutil
import os

class Kopiuj:

    def __init__(self):
        self.zrodlo = "stylus.css"
        self.cel = "/home/qwerty891/Pulpit/strona_internetowa/css/stylus/"
    
    def kopiuj(self):
        shutil.copy(self.zrodlo, self.cel)
        self.zrodlo = "moduly/"
        os.system("cp -r " + self.zrodlo + " " + self.cel)

kopia = Kopiuj()
kopia.kopiuj()
