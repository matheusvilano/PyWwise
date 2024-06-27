def callback(func):
	"""
	A decorator for PyWwise callbacks. Checks if the event in question should be broadcast.
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
