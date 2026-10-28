import ast

from metrics.wmc import calculate_wmc
from metrics.cohesion import calculate_lcom
from metrics.coupling import calculate_cbo
from metrics.rfc import calculate_rfc


def analyze_code(source_code):
    tree = ast.parse(source_code)

    class_nodes = [
        node for node in tree.body
        if isinstance(node, ast.ClassDef)
    ]

    class_names = {node.name for node in class_nodes}

    for node in class_nodes:
        print(f"\nClass: {node.name}")

        for item in node.body:
            if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                print(f"  Method: {item.name}")

        wmc = calculate_wmc(node)
        lcom = calculate_lcom(node)
        cbo, coupled_classes = calculate_cbo(node, class_names)
        rfc = calculate_rfc(node)

        print(f"  WMC: {wmc}")
        print(f"  LCOM: {lcom}")
        print(f"  CBO: {cbo}")
        print(f"  Coupled with: {', '.join(coupled_classes) if coupled_classes else 'None'}")
        print(f"  RFC: {rfc}")