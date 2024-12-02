import ast

def extract_function_names(file_full_path):
    with open(file_full_path, mode='r') as file_obj:
        tree = ast.parse(file_obj.read())
        for flt_node in (node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)):
            print(flt_node.name)

if __name__ == '__main__':
    extract_function_names('test_extraction_function_names.py')

