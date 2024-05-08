# This is an example of a comment, python ignores this and it's used for documentation
import importlib.util
import sys

# The code below loads modules/print.py to call the code later as a print module
spec = importlib.util.spec_from_file_location("module.name", "modules/print.py")
print = importlib.util.module_from_spec(spec)
sys.modules["module.name"] = print
spec.loader.exec_module(print)
# The line below calls the code in modules/print.py
print.printing()

