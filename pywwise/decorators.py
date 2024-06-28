def callback(func):
	"""
	A decorator for PyWwise callbacks. Checks if the associated event is valid and has any subscribers. If it has at
	least one subscriber, it will be broadcast. For the decorated function to work properly: \n
	- its name should start with the prefix `_on_` (e.g. `_on_event_happened`).
	- its associated event should have the same name, minus the prefix `_on_` (e.g. `event_happened`).
	- both the decorated function and the associated event should be encapulated within the same object.
	:param func: The function to decorate.
	:return: The decorated function.
	"""
	
	def wrapper(self, **kwargs):
		event = getattr(self, func.__name__[4:])  # removing the prefix "_on_" gives the RefEvent
		if event is None:
			raise NameError(f"Function '{func.__name__}' missing associated event: '{func.__name__[4:]}'.")
		if len(event) > 0:
			kwargs["event"] = event
			func(self, **kwargs)
	
	return wrapper
