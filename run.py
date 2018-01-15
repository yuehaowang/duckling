 #! /usr/bin/env python3

import runpy, sys, os

import duckling

dklPath = os.path.split(os.path.abspath(sys.argv[0]))[0]

if len(sys.argv) < 2:
	print("Missing a parameter.")
else:
	try:
		os.chdir(os.path.normpath(os.path.join(dklPath, "/".join(sys.argv[1].split(".")))))
		sys.path.insert(0, dklPath)

		runpy.run_path("./main.py", run_name = "__main__")
	except:
		print("Cannot run '%s'." % sys.argv[1])
