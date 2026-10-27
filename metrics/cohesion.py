import ast
from itertools import combinations


def get_method_attributes(method_node):
    attributes = set()

    for node in ast.walk(method_node):
        if isinstance(node, ast.Attribute):
            if isinstance(node.value, ast.Name):
                if node.value.id == "self":
                    attributes.add(node.attr)

    return attributes


def calculate_lcom(class_node):
    methods = []

    for node in class_node.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            methods.append(node)

    if len(methods) < 2:
        return 0

    p = 0
    q = 0

    for method1, method2 in combinations(methods, 2):
        attrs1 = get_method_attributes(method1)
        attrs2 = get_method_attributes(method2)

        if attrs1.intersection(attrs2):
            q += 1
        else:
            p += 1

    return max(0, p - q)