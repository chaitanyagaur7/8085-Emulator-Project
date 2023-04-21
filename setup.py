'''from setuptools import setup, Extension


module = Extension('8085',
                   sources=[#'src/program_counter_increment.py',
                            #'src/dec2hex.py',
                            #'src/hex2dec.py',
                            #'src/string_uppercase.py',
                            #'src/set_flag_register.py',
                            #'src/splitter.py',
                            #'src/initilize_map_opcode.py',
                            #'src/check_opcode.py',
                            
                            #'src/resister_is.py',
                            #'src/check_storage.py',
                            #'src/rpair.py'
                            ],
                   include_dirs=['./header'])

setup(name='8085',
      version='1.0',
      description='8085 emulator',
      ext_modules=[module],
      packages=[''],
      package_data={'': ['src/arithmetic.py',
                         'src/branching.py',
                         'src/debugger.py',
                         'src/global_.py'
                         'src/logical.py',
                         'src/load.py',
                         'src/master.py',
                         'src/tools.py'
                         ]} # add non-C source files here
      )'''
'''import setuptools

setuptools.setup(
    name="my_package",
    version="0.1",
    author="John Doe",
    author_email="johndoe@example.com",
    description="A short description of my package",
    packages=setuptools.find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib"
    ],
)
'''
import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="8085 Emulator",
    version="1.0",
    description="An emulator for 8085 microprocessor.",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)
