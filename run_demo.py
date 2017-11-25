import runpy, sys, os

import duckling


os.chdir("./demo")
sys.path.insert(0, "./")

runpy.run_path("./main.py", run_name = "__main__")
