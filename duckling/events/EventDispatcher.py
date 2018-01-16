from .Event import Event
from ..core.Object import Object 


class EventDispatcher(Object):
	def __init__(self):
		super(EventDispatcher, self).__init__()

		self._eventList = {}

	def addEventListener(self, eventObj, callback):
		self._eventList[eventObj] = callback

	def removeEventListener(self, eventObj, callback):
		for e in self._eventList:
			if e.id == eventObj.id and self._eventList[e] == callback:
				self_eventList.pop(e)

	def removeAllEventListeners(self):
		self._eventList.clear()

	def dispatchEvent(self, eventObj, data = None):
		for e in self._eventList:
			if e.id == eventObj.id:
				eve = eventObj.__class__(eventObj.id)
				eve.currentTarget = self
				eve.data = data

				self._eventList[e](eve)
		