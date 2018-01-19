import functools
import sys, os


log = functools.partial(print, flush = True)

class Path(object):
	@staticmethod
	def getAbsPath(path):
		if os.path.isabs(path):
			return path

		mainPath = os.path.split(os.path.abspath(sys.argv[0]))[0]

		return os.path.normpath(os.path.join(os.path.abspath(mainPath), path))