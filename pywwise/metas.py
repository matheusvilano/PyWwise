class SingletonMeta(type):
	"""Metaclass for singletons."""
	
	_instances = dict()
	"""A dictionary where the keys are classes and the values are instances."""
	
	def __call__(cls, *args, **kwargs):
		"""
		Operator `()`.
		:param args: Positional arguments.
		:param kwargs: Keyword arguments.
		:return: The singleton instance of the `cls` class.
		"""
		if cls not in cls._instances:
			instance = super().__call__(*args, **kwargs)
			cls._instances[cls] = instance
		return cls._instances[cls]
