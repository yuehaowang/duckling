import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from .Object import Object
from ..display.Color import Color
from ..display.OpenGLRenderer2D import OpenGLRenderer2D
from ..display.Sprite import Sprite

from PIL import Image
import numpy
import array


class Game(Object):
	def __init__(self, w = 800, h = 600, title = "Game"):
		super(Game, self).__init__()

		self.windowWidth = w
		self.windowHeight = h
		self.windowTitle = title
		self.backgroundColor = Color(1, 1, 1, 1)
		self.renderer = OpenGLRenderer2D(self)
		self.stage = Sprite()
		self.antialiasing = True

		glutInit(sys.argv)

	def run(self):
		glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)

		self._createWindow()

		glClearColor(*self.backgroundColor.toList())

		self._coordinateProjection()
		self._useAntialiasing()

		glEnable(GL_TEXTURE_2D)

		glutReshapeFunc(self._onWindowResize)
		glutDisplayFunc(self._mainLoop)
		glutIdleFunc(self._mainLoop)
		glutMainLoop()

	def _createWindow(self):
		glutInitWindowSize(self.windowWidth, self.windowHeight)
		glutCreateWindow(self.windowTitle)

	def _coordinateProjection(self):
		w, h = self.windowWidth, self.windowHeight

		glViewport(0, 0, w, h)

		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluOrtho2D(0, w, 0, h)

	def _useAntialiasing(self):
		if self.antialiasing:
			glEnable(GL_BLEND)
			glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
			glEnable(GL_POINT_SMOOTH)
			glEnable(GL_LINE_SMOOTH)
			glEnable(GL_POLYGON_SMOOTH)

	def _onWindowResize(self, newW, newH):
		glutReshapeWindow(self.windowWidth, self.windowHeight)

	def _mainLoop(self):
		glClear(GL_COLOR_BUFFER_BIT)

		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()

		self.stage.display(self.renderer)

		glutSwapBuffers()
