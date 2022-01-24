import os
import sys
import time
import datetime
import locale
import getpass
import platform
import subprocess
class Gk:
    def __init__(self):
        self.os = os.name
        self.sys_lang = locale.getdefaultlocale()
        self.python_ver = sys.version.split()[0]
        self.user_name = getpass.getuser()
        self.version = "1.0"
    def python_ver(self):
        return self.python_ver
    
    def sys_lang(self):
        return self.sys_lang
    
    def os(self):
        return self.os
    
    def clear(self):
        if self.os == "nt":
            os.system("cls")
        else:
            os.system("clear")
            
    def fileexits(self, file):
        if os.path.isfile(file):
            return True
        else:
            return False
        
    def bit(self):
        if platform.machine().endswith('64'):
            return 64
        elif platform.machine().endswith("32"):
            return 32
        
    def direxits(self, dir):
        if os.path.isdir(dir):
            return True
        else:
            return False
        
    def gk_info(self):
        return f"""
Gk3 (Geliştirici Kiti 3) Hakkında

Gk python geliştiriciler kullan daha hızlı ve kolay kod yazmasını sağlamak için yazılmış bir kütüphanedir
yaratıcı: Kerem Ata
lisans: MİT
versiyon: {self.version}
python_versiyonu
"""
    def username(self):
        return self.user_name
    def get_command_output(self,command):
        p = subprocess.run(command, capture_output=True, text=True, shell=True)
        return p.stdout
