from OpenGL.GL import *

from ..core.Object import Object
from .Color import Color
from ..geom.Point2D import Point2D


class OpenGLRenderer2D(Object):
	def __init__(self, parent):
		super(OpenGLRenderer2D, self).__init__()

		self.parent = parent
		self.pathList = []

	def translate(self, x, y):
		glTranslatef(x, y, 0.0)

	def scale(self, scaleX, scaleY):
		glScalef(scaleX, scaleY, 1.0)

	def rotate(self, angle):
		glRotatef(angle, 0.0, 0.0, 1.0)

	def save(self):
		glPushAttrib(GL_ALL_ATTRIB_BITS)
		glPushMatrix()

	def restore(self):
		glPopMatrix()
		glPopAttrib()

	def fill(self):
		glBegin(GL_POLYGON)
		self._drawPath()

	def stroke(self):
		glBegin(GL_LINE_STRIP)
		self._drawPath()

	def closePath(self):
		if len(self.pathList) <= 0:
			return

		path = self.pathList[-1]
		
		if len(path) <= 0:
			return

		p = path[0]

		self.lineTo(p.x, p.y)

	def moveTo(self, x, y):
		self.pathList.append([Point2D(x, y)])

	def lineTo(self, x, y):
		if len(self.pathList) <= 0:
			return

		path = self.pathList[-1]
		path.append(Point2D(x, y))

	def _drawPath(self):
		w, h = self.parent.windowWidth, self.parent.windowHeight

		for path in self.pathList:
			for p in path:
				glVertex2f(p.x, p.y)

		glEnd()

	def setLineWidth(self, lw):
		lw = int(lw)

		if lw >= 1:
			glLineWidth(lw)

	def setColor(self, color):
		if color != None:
			glColor4f(*color.toList())

	def end(self):
		self.pathList.clear()

	def drawImage(self, img, aX, aY, aW, aH):
		imgW, imgH = img.size

		right, top = aX + aW, aY + aH

		if right > imgW:
			right = imgW
		if top > imgH:
			top = imgH

		lRatio, bRatio = (aX / imgW if aX <= imgW else 1), (aY / imgH if aY < imgH else 1)
		rRatio, tRatio = (right / imgW if right <= imgW else 1), (top / imgH if top <= imgH else 1)

		id = glGenTextures(1)
		glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
		glBindTexture(GL_TEXTURE_2D, id)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
		glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, imgW, imgH, 0, GL_RGBA, GL_UNSIGNED_BYTE, img.tobytes())

		glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE,GL_REPLACE)
		glBindTexture(GL_TEXTURE_2D, id)

		glBegin(GL_QUADS)
		glTexCoord2f(lRatio, bRatio)
		glVertex2f(0, 0)
		glTexCoord2f(rRatio, bRatio)
		glVertex2f(aW, 0)
		glTexCoord2f(rRatio, tRatio)
		glVertex2f(aW, aH)
		glTexCoord2f(lRatio, tRatio)
		glVertex2f(0, aH)
		glEnd()
		