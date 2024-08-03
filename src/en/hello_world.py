# Import the obspython module
import obspython as obs

# The Python Module Search Path will be displayed in the Script Log Window
import sys
obs.script_log(obs.LOG_INFO, str(sys.path))