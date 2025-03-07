# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from typing import Iterator as _Iterator, Self as _Self

from pywwise.aliases import RegexPattern
from pywwise.enums import EObjectType, EWaqlSelectExpression
from pywwise.primitives import GUID, Name, ProjectPath, ShortID
from pywwise.structs import WaqlCondition


class WAQL:
    """
    A helper class listing common WAQL statements. Utility functions are available to help build queries. Queries may
    be built without this class, but if you are unfamiliar with WAQL, it can be a time-saver. Useful features:\n
    - To print the query, simply pass the query to the `print` function (or similar). Example: `print(my_waql_object)`.
    - To get the generated query, convert the instance to a `str`. Example: `str(my_waql_object)`.
    - To get and set a specific query item (statement), you can use the regular `[]` (subscription) operator, like with
      lists, tuples, etc. Example: `my_waql_object[0]`.
    - To delete a specific query item (statement), you can use the regular `del` (delete) operator. Example:
      `del my_waql_obj`.
    If you are interested in how exactly this class works: it encapsulates a list of strings (`list[str]`) and most
    methods are just sugar syntax for appending `str` objects (which are WAQL "statements") to the list. There are also
    overrides for "magic methods" to allow for some of the syntax the features described in this docstring.
    """
    
    def __init__(self):
        """Constructor for WAQL queries. To build a query, instantiate a WAQL object, then use the objects methods."""
        self._statements: list[str] = []
    
    def __str__(self) -> str:
        """:return: The query (all statements), formatted as a string."""
        return f"$ {' '.join(self._statements)}"
    
    def __getitem__(self, index: int) -> str:
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
    
    def __iter__(self) -> _Iterator[str]:
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
    
    def __add__(self, statement: str) -> _Self:
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
    def _where(property_name: str, bool_operator: str,
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
    
    def where(self, condition: WaqlCondition):
        """
        Filters objects of the input sequence by rejecting objects that don't match the specified expression. For
        chaining conditions, see `and_where`, `or_where`.
        :param condition: The condition to evaluate.
        """
        statement = f"{self._where(condition.property_name, condition.bool_operator, condition.value_or_ref_or_regex)}"
        self._statements.append(statement)
    
    def and_where(self, condition: WaqlCondition):
        """
        Use after `where` to append a condition with `and`.
        :param condition: The condition to evaluate.
        """
        statement = f"{self._where(condition.property_name, condition.bool_operator, condition.value_or_ref_or_regex)}"
        self._statements.append(statement)
    
    def or_where(self, condition: WaqlCondition):
        """
        Use after `where` to append a condition with `or`.
        :param condition: The condition to evaluate.
        """
        statement = f"{self._where(condition.property_name, condition.bool_operator, condition.value_or_ref_or_regex)}"
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
    
    def select(self, *expressions_or_property_names: EWaqlSelectExpression | str):
        """
        Returns an object or list of objects based on the specified expressions and Names.
        :param expressions_or_property_names: The expressions and/or property names to use.
        """
        statement = "select "
        for ex_or_prop in expressions_or_property_names:
            statement += f"{ex_or_prop}, "
        statement = statement.rstrip(", ")
        self._statements.append(statement)
