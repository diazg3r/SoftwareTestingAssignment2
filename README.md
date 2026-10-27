# SoftwareTestingAssignment2

A Python-based software testing tool designed to analyze object-oriented code and calculate software quality metrics. The tool uses Python's Abstract Syntax Tree (AST) module to examine class definitions without executing the source code.

WMC (Weighted Methods per Class): Measures the number and complexity of methods in a class.


LCOM (Lack of Cohesion of Methods): Measures how closely related the methods of a class are.


CBO (Coupling Between Objects): Measures dependencies between classes.


RFC (Response for a Class): Measures the methods that may execute in response to a method call.




How It Works
The user provides a Python file or pastes class definitions.
The tool analyzes the code using AST.
Each metric module calculates its respective values.
The results are displayed in the terminal.



Purpose
Developed for a Software Testing assignment to demonstrate the implementation and integration of object-oriented software metrics.
