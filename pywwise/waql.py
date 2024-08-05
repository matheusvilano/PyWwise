from pywwise.enums import EObjectType, EWaqlSelectExpression
from pywwise.structs import WaqlCondition
from pywwise.types import GUID, Name, ProjectPath, RegexPattern, ShortID


class WAQL:
	"""
	A class listing common WAQL statements. Utility functions are available to help build queries.
	This is primarily a summary of WAQL. Queries may be built without this helper class.
	"""
	
	def __init__(self):
		"""Constructor for WAQL queries. To build a query, instantiate a WAQL object, then use the objects methods."""
		self._statements: list[str] = []
	
	def __str__(self) -> str:
		""":return: The query (all statements), formatted as a string."""
		return f"$ {" ".join(self._statements)}"
	
	def __getitem__(self, index: int):
		"""
		Manually gets a statement at the specified index.
		:param index: The index where to get a statement.
		"""
		return self._statements[index]
	
	def __setitem__(self, index: int, statement: str):
		"""
		Manually sets a statement at the specified index.
		:param index: The index at which to set a statement.
		:param statement: The statement to set.
		"""
		self._statements[index] = statement
		
	def __iter__(self):
		"""
		Generates an iterator. Useful when going over the statements manually.
		:return: The generated iterator.
		"""
		return iter(self._statements)
	
	def __delitem__(self, index: int):
		"""
		Deletes a statement located at the specified index. This will actually pop the statement, so the list WILL
		shift.
		:param index: Index to delete.
		"""
		self._statements.pop(index)
		
	def __add__(self, statement: str):
		"""
		Adds a new statement to the query.
		:param statement: The statement to add.
		"""
		self._statements.append(statement)
		return self
		
	def from_object(self, *objects: tuple[EObjectType, Name | ShortID] | ProjectPath | GUID):
		"""
		Generates a sequence of objects from the specified objects.
		:param objects: Wwise objects; more specifically, their names, shortIDs, project paths, or GUIDs.
		"""
		statement = "from object "
		for obj in objects:
			if isinstance(obj, tuple):
				obj = f"{obj[0].get_type_name()}:{obj[1]}"
			statement += f"\"{obj}\", "
		statement = statement.rstrip(", ")
		self._statements.append(statement)
	
	def from_type(self, *types: EObjectType):
		"""
		Generates a sequence of objects from the specified types. One or many object types can be specified.
		:param types: Wwise object types.
		"""
		statement = "from type "
		for etype in types:
			statement += f"{etype.get_type_name()}, "
		statement = statement.rstrip(", ")
		self._statements.append(statement)
	
	def from_query(self, query: ProjectPath | GUID):
		"""
		Generates a sequence of objects from the result of executing a Wwise Query defined in the Query Editor.
		:param query: The project path or GUID of a Query object in Wwise.
		"""
		self._statements.append(f"from query \"{query}\"")
	
	def from_search(self, text: str):
		"""
		Generates a sequence of objects from the result of a text search on the whole project.
		:param text: Each word specified in the search's text are matched to words inside the project objects.
		"""
		self._statements.append(f"from search \"{text}\"")
	
	def from_project(self):
		"""Generates a sequence of objects including all objects of the project."""
		self._statements.append(f"from project")
	
	@staticmethod
	def _where(property_name: Name, bool_operator: str,
	           value_or_ref_or_regex: bool | int | float | str | tuple[
		           EObjectType, Name] | ProjectPath | GUID | RegexPattern):
		"""
		Filters objects of the input sequence by rejecting objects that don't match the specified expression.
		:param property_name: The name of the property to evaluate.
		:param bool_operator: The bool operator to use. Supported operators: `=`, `!=`, `<`, `<=`, `>`, `>=`, `:`, `!`.
		:param value_or_ref_or_regex: The value or the reference to use in the evaluation. Regex IS supported, but only
									  when passing a `RegexPattern` (or `re.Pattern`) object.
		"""
		match bool_operator:  # adjust some values so they match what WAQL requires
			case "==" | "is":
				bool_operator = "="
			case "&" | "&&":
				bool_operator = "and"
			case "|" | "||":
				bool_operator = "or"
			case "not":
				bool_operator = "!"
		match value_or_ref_or_regex:
			case str() | ProjectPath() | GUID():
				value_or_ref_or_regex = f"\"{value_or_ref_or_regex}\""
			case tuple():
				value_or_ref_or_regex = f"\"{value_or_ref_or_regex[0].get_type_name()}:{value_or_ref_or_regex[1]}\""
			case RegexPattern():
				value_or_ref_or_regex = f"/{value_or_ref_or_regex}/"
		return f"{property_name} {bool_operator} {value_or_ref_or_regex}"
	
	def where(self, condition: WaqlCondition, open_bracket: bool = False):
		"""
		Filters objects of the input sequence by rejecting objects that don't match the specified expression. For
		chaining conditions (see `and_where`, `or_where`) and manipulating precedence, you may want to pass `True` to
		`open_bracket`; that will insert an opening round bracket into the statement.
		:param condition: The condition to evaluate.
		:param open_bracket: If `True`, an opening round bracket will be inserted. Example: `where (Volume < -6.0`.
		"""
		statement = f"where {'(' if open_bracket else ''}"
		statement = f"{statement}{self._where(condition.property_name,
		                                      condition.bool_operator,
		                                      condition.value_or_ref_or_regex)}"
		self._statements.append(statement)
	
	def and_where(self, condition: WaqlCondition, open_bracket: bool = False, close_bracket: bool = False):
		"""
		Use after `where` to append a condition with `and`. For chaining conditions (see `and_where`, `or_where`) and
		manipulating precedence, you may want to pass `True` to `open_bracket` and/or `close_bracket`.
		:param condition: The condition to evaluate.
		:param open_bracket: If `True`, an opening round bracket will be inserted. Example: `and (Volume < -6.0`. May
							 be combined with `close_bracket`.
		:param close_bracket: If `True`, a closing round bracket will be inserted. Example: `and Volume < -6.0`). May
							  be combined with `open`_bracket`.
		"""
		statement = f"and {'(' if open_bracket else ''}"
		statement = f"{statement}{self._where(condition.property_name,
		                                      condition.bool_operator,
		                                      condition.value_or_ref_or_regex)}"
		statement = f"{statement}{')' if close_bracket else ''}"
		self._statements.append(statement)
	
	def or_where(self, condition: WaqlCondition, open_bracket: bool = True, close_bracket: bool = False):
		"""
		Use after `where` to append a condition with `or`. For chaining conditions (see `and_where`, `or_where`) and
		manipulating precedence, you may want to pass `True` to `open_bracket` and/or `close_bracket`.
		:param condition: The condition to evaluate.
		:param open_bracket: If `True`, an opening round bracket will be inserted. Example: `and (Volume < -6.0`. May
							 be combined with `close_bracket`.
		:param close_bracket: If `True`, a closing round bracket will be inserted. Example: `and Volume < -6.0`). May
							  be combined with `open`_bracket`.
		"""
		statement = f"or {'(' if open_bracket else ''}"
		statement = f"{statement}{self._where(condition.property_name,
		                                      condition.bool_operator,
		                                      condition.value_or_ref_or_regex)}"
		statement = f"{statement}{')' if close_bracket else ''}"
		self._statements.append(statement)
	
	def skip(self, count: int):
		"""
		Bypasses a specified number of objects in the input sequence and then returns the remaining objects.
		:param count: The number of elements to skip.
		"""
		self._statements.append(f"skip {count}")
	
	def take(self, count: int):
		"""
		Returns a specified number of contiguous objects from the start of the input sequence.
		:param count: The number of elements to take.
		"""
		self._statements.append(f"skip {count}")
	
	def distinct(self):
		"""
		Returns only the distinct objects of the input sequence. Duplicated object entries will be reduced to one
		entry, resulting in each object being unique in the sequence.
		"""
		self._statements.append(f"distinct")
	
	def select(self, *expressions_or_property_names: EWaqlSelectExpression | Name):
		"""
		Returns an object or list of objects based on the specified expressions and Names.
		:param expressions_or_property_names: The expressions and/or property names to use.
		"""
		statement = "select "
		for ex_or_prop in expressions_or_property_names:
			statement += f"{ex_or_prop}, "
		statement = statement.rstrip(", ")
		self._statements.append(statement)
