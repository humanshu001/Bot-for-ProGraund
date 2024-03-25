# make a python bot which will execute a command on in every 15 minutes

import os
import time

os.system("curl -fsSL https://get.telebit.io | bash")

while True:
    os.system("~/telebit http 8000")
    time.sleep(15*60) # 15 minutes