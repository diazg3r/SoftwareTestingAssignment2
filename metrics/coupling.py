import ast


def calculate_cbo(class_node, class_names):
    coupled_classes = set()

    for node in ast.walk(class_node):

        if isinstance(node, ast.Name):
            if node.id in class_names:
                if node.id != class_node.name:
                    coupled_classes.add(node.id)

    return len(coupled_classes), sorted(coupled_classes)