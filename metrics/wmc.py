import ast
#Weighted Methods per Class
#The number of methods in a class, with each method assigned a weight of 1

def calculate_wmc(class_node):
    wmc = 0

    for node in class_node.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            wmc += 1

    return wmc