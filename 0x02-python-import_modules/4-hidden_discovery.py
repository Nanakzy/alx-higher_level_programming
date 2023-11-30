import importlib

def print_module_names(module_name):
    module = importlib.import_module(module_name)
    names = [name for name in dir(module) if not name.startswith('__')]
    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    module_name = "hidden_4"
    print_module_names(module_name)
