import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from .Object import Object
from .Keyboard import Keyboard
from ..display.Color import Color
from ..display.OpenGLRenderer2D import OpenGLRenderer2D
from ..display.DisplayObject import DisplayObject
from ..display.Sprite import Sprite
from ..events.KeyboardEvent import KeyboardEvent


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
		self.enableDoubleBuffer = True
		self.fps = 60

		self.stage.parent = DisplayObject.PARENT_ROOT

		glutInit(sys.argv)

	def run(self):
		glutInitDisplayMode(GLUT_RGBA | (GLUT_DOUBLE if self.enableDoubleBuffer else GLUT_SINGLE))

		self._createWindow()

		glClearColor(*self.backgroundColor.toList())

		self._coordinateProjection()
		self._useAntialiasing()

		glEnable(GL_TEXTURE_2D)

		glutReshapeFunc(self._onWindowResize)
		glutDisplayFunc(self._loopDraw)
		glutTimerFunc(0, self._enterLoopEvent, 0)
		glutSpecialFunc(self._enterKeyboardKeyDownEvent)
		glutKeyboardFunc(self._enterKeyboardKeyDownEvent)
		glutSpecialUpFunc(self._enterKeyboardKeyUpEvent)
		glutKeyboardUpFunc(self._enterKeyboardKeyUpEvent)
		glutMouseFunc(self._enterMouseButtonEvent)
		glutMotionFunc(self._enterMouseMotionEvent)
		glutPassiveMotionFunc(self._enterMouseMotionEvent)
		glutMainLoop()

	def exit(self, code = 0):
		sys.exit(code)

	def _createWindow(self):
		glutInitWindowSize(self.windowWidth, self.windowHeight)
		glutCreateWindow(self.windowTitle.encode("utf-8"))

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

	def _loopDraw(self):
		glClear(GL_COLOR_BUFFER_BIT)

		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()

		self.stage.display(self.renderer)

		if self.enableDoubleBuffer:
			glutSwapBuffers()
		else:
			glFlush()

	def _enterLoopEvent(self, v):
		self.stage._enterLoopEvent()

		if self.fps > 0:
			glutPostRedisplay()
			glutTimerFunc(1000 // self.fps, self._enterLoopEvent, 0)

	def _enterKeyboardKeyDownEvent(self, key, mouseX, mouseY):
		self.stage.dispatchEvent(KeyboardEvent.KEY_DOWN, {"key" : key})

	def _enterKeyboardKeyUpEvent(self, key, mouseX, mouseY):
		self.stage.dispatchEvent(KeyboardEvent.KEY_UP, {"key" : key})

	def _enterMouseButtonEvent(self, button, state, mouseX, mouseY):
		eve = {
			"button" : button,
			"state" : state,
			"mouseX" : mouseX,
			"mouseY" : self.windowHeight - mouseY
		}
		
		self.stage._enterMouseEvent(eve, self.stage.getMatrix())

	def _enterMouseMotionEvent(self, mouseX, mouseY):
		eve = {
			"mouseX" : mouseX,
			"mouseY" : self.windowHeight - mouseY
		}

		self.stage._enterMouseEvent(eve, self.stage.getMatrix())
