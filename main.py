# This is an example of a comment, python ignores this and it's used for documentation
# The code below imports the sys and importlib.util library to be used to lookup files
import importlib.util
import sys

# The code below loads modules/print.py to call the code later as a print module
spec = importlib.util.spec_from_file_location("module.name", "modules/print.py")
printer = importlib.util.module_from_spec(spec)
sys.modules["module.name"] = printer
spec.loader.exec_module(printer)
# The line below calls the code in modules/print.py
print("Preparing to run print module")
printer.printing()


# The code below loads modules/variables.py to call the code later as a variables module
spec = importlib.util.spec_from_file_location("module.name", "modules/variables.py")
variables = importlib.util.module_from_spec(spec)
sys.modules["module.name"] = variables
spec.loader.exec_module(variables)
# The line below calls the code in modules/print.py
print("Preparing to run variables module")
variables.variables()

# The code below loads modules/loop.py to call the code later as a loop module
spec = importlib.util.spec_from_file_location("module.name", "modules/loop.py")
loop = importlib.util.module_from_spec(spec)
sys.modules["module.name"] = loop
spec.loader.exec_module(loop)
# The line below calls the code in modules/loop.py
print("Preparing to run loop module")
loop.loop()
