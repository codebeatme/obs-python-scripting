# Import the obspython module
import obspython as obs

def script_description():
    return 'This is a simple but ineffective script\nAuthor:\toops\nVersion:\t0.1\nContact:\txxx'

def script_properties():
    # Create a Property Set object
    props = obs.obs_properties_create()

    # Add a Script Property object that corresponds to the numberbox for indicating hours
    obs.obs_properties_add_int(props, 'hours', '小时：', 2, 5, 1)
    return props

# The data variable represents the Script Settings
data = None

def script_load(settings):
    global data
    data = settings

    # Read the Script Setting Item closed_time, which is the stop-time of the script
    closed_time = obs.obs_data_get_string(data, 'closed_time')
    if closed_time:
        obs.script_log(obs.LOG_INFO, f'The last time the script stopped was at {closed_time}')

    obs.script_log(obs.LOG_INFO, script_path())

# def script_unload():
#     # Write the current time to the Script Setting Item closed_time as the stop-time of the script
#     from datetime import datetime
#     obs.obs_data_set_string(data, 'closed_time', datetime.now().ctime())

def script_update(settings):
    # Read the Script Setting Item hours and display it
    hours = obs.obs_data_get_int(settings, 'hours')
    obs.script_log(obs.LOG_INFO, f'The current hours are {hours}')

def script_save(settings):
	# Write the current time to the Script Setting Item closed_time as the stop time of the script
	from datetime import datetime
	obs.obs_data_set_string(settings, 'closed_time', datetime.now().ctime())

def script_defaults(settings):
	# Set the default value of the Setting Item hours to 3
	obs.obs_data_set_default_int(settings, 'hours', 3)

# def script_tick(seconds):
# 	obs.script_log(obs.LOG_INFO, f'{seconds} OBS is about to become unresponsive!!!')
     
# Script Timer callback function welcome
def welcome():
    obs.script_log(obs.LOG_INFO, f'{type(obs.timer_add)}')
    obs.script_log(obs.LOG_INFO, 'This is a callback function that is only called once')
    # Remove the Script Timer corresponding to welcome
    obs.remove_current_callback()

# Add a Script Timer with a 3-second interval
obs.timer_add(welcome, 3000)