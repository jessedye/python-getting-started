# This is an example of a comment, python ignores this and it's used for documentation
# The code below imports the sys and importlib.util library to be used to lookup files
import importlib.util
import sys

# The below is an example variable feel free to change it
name = "Jesse"
# Example variable but a number
number = 10

# The code below loads modules/print.py to call the code later as a print module
spec = importlib.util.spec_from_file_location("module.name", "modules/print.py")
printer = importlib.util.module_from_spec(spec)
sys.modules["module.name"] = printer
spec.loader.exec_module(printer)
print("Preparing to run print module")
# The line below calls the code in modules/print.py as a Function
printer.printing()


# The code below loads modules/variables.py to call the code later as a variables module
spec = importlib.util.spec_from_file_location("module.name", "modules/variables.py")
variables = importlib.util.module_from_spec(spec)
sys.modules["module.name"] = variables
spec.loader.exec_module(variables)
print("Preparing to run variables module")
# The line below calls the code in modules/variables.py as a Function
variables.variables(name)

# The code below loads modules/loop.py to call the code later as a loop module
spec = importlib.util.spec_from_file_location("module.name", "modules/loop.py")
loop = importlib.util.module_from_spec(spec)
sys.modules["module.name"] = loop
spec.loader.exec_module(loop)
# The line below calls the code in modules/loop.py as a Function
print("Preparing to run loop module")
loop.loop()

# The code below loads modules/logic-operators.py to call the code later as a logic module
spec = importlib.util.spec_from_file_location("module.name", "modules/logic-operators.py")
logic = importlib.util.module_from_spec(spec)
sys.modules["module.name"] = logic
spec.loader.exec_module(logic)
print("Preparing to run logic module")
# The line below calls the code in modules/logic-operators.py as a Function
# sets logic variable to Jesse that gets passed to modules/logic-operators.py as an Argument
logic.logic(name)

# The code below loads modules/math.py to call the code later as a logic module
spec = importlib.util.spec_from_file_location("module.name", "modules/math.py")
math = importlib.util.module_from_spec(spec)
sys.modules["module.name"] = math
spec.loader.exec_module(math)
print("Preparing to run math module")
# The line below calls the code in modules/math.py as a Function
# sets logic variable to Jesse that gets passed to modules/maths.py as an Argument
math.math(number)
