import os,time,random
from time import sleep
from setuptools import setup
from Cython.Build import cythonize
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
ti = (' \x1b[1;94m{\x1b[1;91m•\x1b[1;94m}\x1b[1;97m ')
pl = (' \x1b[1;92m{\x1b[1;97m+\x1b[1;92m}\x1b[1;97m ')
banner = (f'''
{M}+---------------------------------------------+
  {ti}{P}AUTHOR : XENZ
  {ti}{P}GITHUB : https://github.com/Xenz-11
  {ti}{P}TEAM   : SPY CYBER TEAM
{M}+---------------------------------------------+

        {P}COMPILE PYTHON 3
''')
try:
    os.system('clear')
    print (banner)
    file = input(f'{pl}INPUT FILE : {H}')
    xenz = file.replace('.py','')
    setup(
        ext_modules = cythonize(file,compiler_directives={'language_level' : "3"})
    )
    os.system('clear')
    print (banner)
    for i in range(101):
        sleep(0.02)
        wa = random.choice([M,K,H,B])
        bi = (' \x1b[1;97m{'+wa+'*\x1b[1;97m}')
        print (bi,'LOADING ',i,'%',end='\r')
    print (f' {ti} COMPILE SUCCESS : {H}'+xenz+'.cpython-310.so')
    print (f' {ti} THANKS FOR USING MY TOOLS >_<')
except ValueError:
    print(' \x1b[1;92m{\x1b[1;91m×\x1b[1;92m} \x1b[1;97mFILE NOT FOUND')
