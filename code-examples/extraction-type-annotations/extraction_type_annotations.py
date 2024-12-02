import ast

def extract_type_annotations(file_full_path):
    with open(file_full_path, mode='r') as file_obj:
        tree = ast.parse(file_obj.read())
        for flt_node in (node for node in ast.walk(tree) if isinstance(node, ast.AnnAssign)):
            print()
            print('Processing annotated assignment for variable:', flt_node.target.id)
            try:
                print('Type annotation:', flt_node.annotation.id)
            except AttributeError: 
                print('Type annotation:', flt_node.annotation.value.id)

if __name__ == '__main__':
    extract_type_annotations('test_extraction_type_annotations.py')

