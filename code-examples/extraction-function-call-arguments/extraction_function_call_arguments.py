import ast

def extract_function_call_arguments(file_full_path, target_func_name='my_func_1'):
    with open(file_full_path, mode='r') as file_obj:
        tree = ast.parse(file_obj.read())
        for flt_node in (node for node in ast.walk(tree) if isinstance(node, ast.Call) and node.func.id==target_func_name):
            print()
            print('Processing function call', flt_node.func.id, 'at line', flt_node.lineno)
            if all(isinstance(arg, ast.Constant) and isinstance(arg.value, str) for arg in flt_node.args):
                print('All input arguments are strings - Values:')
                for arg in flt_node.args: print(arg.value)
            else:
                print('Not all input arguments are strings!')

if __name__ == '__main__':
    extract_function_call_arguments('test_extraction_function_call_arguments.py')

