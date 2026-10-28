import ast


def calculate_rfc(class_node):
    defined_methods = set()
    called_methods = set()

    for node in class_node.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            defined_methods.add(node.name)

            for child in ast.walk(node):
                if isinstance(child, ast.Call):

                    if isinstance(child.func, ast.Attribute):
                        called_methods.add(child.func.attr)

    response_set = defined_methods.union(called_methods)

    return len(response_set)

#The original program use to could print() as a function, so we were having not accurate information