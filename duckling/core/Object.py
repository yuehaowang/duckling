class Object(object):
	object_index = 0

	def __init__(self):
		super(Object, self).__init__()

		Object.object_index += 1
		self.objectIndex = Object.object_index
