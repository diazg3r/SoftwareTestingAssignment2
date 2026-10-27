import ast
from metrics.wmc import calculate_wmc
from metrics.cohesion import calculate_lcom


def analyze_code(source_code):
    tree = ast.parse(source_code)

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            print(f"\nClass: {node.name}")

            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    print(f"  Method: {item.name}")

            wmc = calculate_wmc(node)
            lcom = calculate_lcom(node)

            print(f"  WMC: {wmc}")
            print(f"  LCOM: {lcom}")