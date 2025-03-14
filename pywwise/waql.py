# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from typing import Iterator as _Iterator, Self as _Self

from pywwise.aliases import RegexPattern
from pywwise.enums import EObjectType, EWaqlLogicalOperator, EWaqlSelectExpression
from pywwise.primitives import GUID, Name, ProjectPath, ShortID


class WaqlQuery:
    """
    A helper class for building WAQL queries. Queries may be built without this class, which is actually preferred;
    but if you are unfamiliar with WAQL, this class can be a time-saver. Useful features:\n
    - To print the query, simply pass the query to the `print` function (or similar). Example: `print(my_waql_object)`.
    - To get the generated query, convert the instance to a `str`. Example: `str(my_waql_object)`.
    - To get and set a specific query component, you can use the regular `[]` (subscription) operator, like with lists,
    tuples, etc. Example: `my_waql_object[0]`.
    - To delete a specific query component, you can use the regular `del` (delete) operator. Example: `del my_waql_obj`.
    If you are interested in how exactly this class works: it encapsulates a list of strings (`list[str]`) and most
    methods are just sugar syntax for appending `str` objects (most of which are WAQL "components") to the list. There
    are also overrides for "magic methods" to allow for some of the syntax the features described in this docstring.
    """
    
    def __init__(self):
        """Constructor for WAQL queries. To build a query, instantiate a WAQL object, then use the objects methods."""
        self._components: list[str] = []
    
    def __str__(self) -> str:
        """:return: The query (all components), formatted as a string."""
        return f"$ {' '.join(self._components)}"
    
    def __repr__(self) -> str:
        """:return: The query (all components), formatted as a string."""
        return self.__str__()
    
    def __getitem__(self, index: int) -> str:
        """
        Manually gets a component at the specified index.
        :param index: The index where to get a component.
        """
        return self._components[index]
    
    def __setitem__(self, index: int, component: str):
        """
        Manually sets a component at the specified index.
        :param index: The index at which to set a component.
        :param component: The component to set.
        """
        self._components[index] = component
    
    def __iter__(self) -> _Iterator[str]:
        """
        Generates an iterator. Useful when going over the components manually.
        :return: The generated iterator.
        """
        return iter(self._components)
    
    def __delitem__(self, index: int):
        """
        Deletes a component located at the specified index. This will actually pop the component, so the list WILL
        shift.
        :param index: Index to delete.
        """
        self._components.pop(index)
    
    def __add__(self, component: str) -> _Self:
        """
        Adds a new component to the query.
        :param component: The component to add.
        """
        self._components.append(component)
        return self
    
    def from_object(self, *objects: tuple[EObjectType, Name | ShortID] | ProjectPath | GUID):
        """
        Generates a sequence of objects from the specified objects.
        :param objects: Wwise objects; more specifically, their names, shortIDs, project paths, or GUIDs.
        """
        component = "from object "
        for obj in objects:
            if isinstance(obj, tuple):
                obj = f"{obj[0].get_type_name()}:{obj[1]}"
            component += f"\"{obj}\", "
        component = component.rstrip(", ")
        self._components.append(component)
    
    def from_type(self, *types: EObjectType):
        """
        Generates a sequence of objects from the specified types. One or many object types can be specified.
        :param types: Wwise object types.
        """
        component = "from type "
        for etype in types:
            component += f"{etype.get_type_name()}, "
        component = component.rstrip(", ")
        self._components.append(component)
    
    def from_query(self, query: ProjectPath | GUID):
        """
        Generates a sequence of objects from the result of executing a Wwise Query defined in the Query Editor.
        :param query: The project path or GUID of a Query object in Wwise.
        """
        self._components.append(f"from query \"{query}\"")
    
    def from_search(self, text: str):
        """
        Generates a sequence of objects from the result of a text search on the whole project.
        :param text: Each word specified in the search's text are matched to words inside the project objects.
        """
        self._components.append(f"from search \"{text}\"")
    
    def from_project(self):
        """Generates a sequence of objects including all objects of the project."""
        self._components.append(f"from project")
    
    def skip(self, count: int):
        """
        Bypasses a specified number of objects in the input sequence and then returns the remaining objects.
        :param count: The number of elements to skip.
        """
        self._components.append(f"skip {count}")
    
    def take(self, count: int):
        """
        Returns a specified number of contiguous objects from the start of the input sequence.
        :param count: The number of elements to take.
        """
        self._components.append(f"skip {count}")
    
    def distinct(self):
        """
        Returns only the distinct objects of the input sequence. Duplicated object entries will be reduced to one
        entry, resulting in each object being unique in the sequence.
        """
        self._components.append(f"distinct")
    
    def select(self, *expressions_or_property_names: EWaqlSelectExpression | str):
        """
        Returns an object or list of objects based on the specified expressions and Names.
        :param expressions_or_property_names: The expressions and/or property names to use.
        """
        component = "select "
        for ex_or_prop in expressions_or_property_names:
            component += f"{ex_or_prop}, "
        component = component.rstrip(", ")
        self._components.append(component)
    
    def where(self):
        """
        Adds "where" to your query. Use this in combination with **expression**, **and_expression**, **or_expression**,
        **open_bracket**, and **close_bracket** to create either simple or compound expressions.
        """
        self._components.append("where")
    
    def expression(self, property_name: str, logic_operator: EWaqlLogicalOperator | str,
                   value_or_ref_or_regex: bool | int | float | str | tuple[
                       EObjectType, Name] | ProjectPath | GUID | RegexPattern):
        """
        Filters objects of the input sequence by rejecting objects that don't match the specified expression.
        :param property_name: The name of the property to evaluate.
        :param logic_operator: The bool operator to use. Supported operators: `=`, `!=`, `<`, `<=`, `>`, `>=`, `:`.
        :param value_or_ref_or_regex: The value or the reference to use in the evaluation. Regex IS supported, but only
                                      when passing a `RegexPattern` (or `re.Pattern`) object.
        """
        if logic_operator == "==":  # Fixing common user mistake :)
            logic_operator = EWaqlLogicalOperator.EQUAL
        if str(logic_operator) not in EWaqlLogicalOperator:
            raise ValueError(f"Invalid logic operator for WAQL: '{logic_operator}'")
        match value_or_ref_or_regex:
            case str() | ProjectPath() | GUID():
                value_or_ref_or_regex = f"\"{value_or_ref_or_regex}\""
            case tuple():
                value_or_ref_or_regex = f"\"{value_or_ref_or_regex[0].get_type_name()}:{value_or_ref_or_regex[1]}\""
            case RegexPattern():
                value_or_ref_or_regex = f"/{value_or_ref_or_regex}/"
        self._components.append(f"{property_name} {logic_operator} {value_or_ref_or_regex}")
    
    def and_operator(self):
        """
        Append **and** to your query. Use this in combination with **expression**, **and_expression**, **or_expression**,
        **open_bracket**, and **close_bracket** to create compound expressions.
        """
        self._components.append("and")
    
    def or_operator(self):
        """
        Append **or** to your query. Use this in combination with **expression**, **and_expression**, **or_expression**,
        **open_bracket**, and **close_bracket** to create compound expressions.
        """
        self._components.append("or")
    
    def open_bracket(self):
        """
        Insert an open round bracket **("(")** into your query. Use this in combination with **expression**,
        **and_expression**, **or_expression**, **open_bracket**, and **close_bracket** to create compound expressions.
        """
        self._components.append("(")
    
    def close_bracket(self):
        """
        Insert an open round bracket **(")")** into your query. Use this in combination with **expression**,
        **and_expression**, **or_expression**, **open_bracket**, and **close_bracket** to create compound expressions.
        """
        self._components.append(")")
