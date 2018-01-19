'''

This script is used for testing demo and examples under the situation that you modified the code of duckling engine and want to check how it works without re-installing it.

Usage:
	* Run `./test.py path/to/target`.
	* e.g. If you want to test demo 'hello_world', run `./test.py demo/hello_world` in your terminal.

Note:
	* It's feasible to add your own demo or examples for testing.
	* Each demo or example requires 'main.py' as the program entrance.

'''

#! /usr/bin/env python3

import runpy, sys, os, logging

import duckling


dklPath = os.path.split(os.path.abspath(sys.argv[0]))[0]

if len(sys.argv) < 2:
	print("Missing a parameter.")
else:
	try:
		os.chdir(os.path.normpath(os.path.join(dklPath, sys.argv[1])))
		sys.path.insert(0, dklPath)

		runpy.run_path("./main.py", run_name = "__main__")
	except Exception as e:
		logging.exception(e)

		print("\nCannot run '%s' because of the exception above.\n" % sys.argv[1])
