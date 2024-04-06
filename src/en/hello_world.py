# Import the obspython module
import obspython as obs

# The Python module search path will be displayed in the Script Log Window
import sys
obs.script_log(obs.LOG_INFO, str(sys.path))