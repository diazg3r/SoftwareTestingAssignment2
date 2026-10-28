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

                    elif isinstance(child.func, ast.Name):
                        called_methods.add(child.func.id)

    response_set = defined_methods.union(called_methods)

    return len(response_set)