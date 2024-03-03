# 导入模块 obspython
import obspython as obs

def script_description():
    return '这是一个简单但没有任何效果的脚本\n作者：\t哎呦喂\n版本：\t0.1\n联系：\txxx'

def script_properties():
    # 创建一个属性集对象
    props = obs.obs_properties_create()

    # 添加一个对应数字显示框的脚本属性对象，用于表示小时
    obs.obs_properties_add_int(props, 'hours', '小时：', 2, 5, 1)
    return props

# 变量 data 表示脚本设置
data = None

def script_load(settings):
    global data
    data = settings

    # 读取脚本设置项 closed_time，他是脚本的停止时间
    closed_time = obs.obs_data_get_string(data, 'closed_time')
    if closed_time:
        obs.script_log(obs.LOG_INFO, f'上次脚本停止的时间为 {closed_time}')

# def script_unload():
#     # 将当前时间写入脚本设置项 closed_time，作为脚本的停止时间
#     from datetime import datetime
#     obs.obs_data_set_string(data, 'closed_time', datetime.now().ctime())

def script_update(settings):
    # 读取脚本设置项 hours 并显示
    hours = obs.obs_data_get_int(settings, 'hours')
    obs.script_log(obs.LOG_INFO, f'当前小时为 {hours}')

def script_save(settings):
	# 将当前时间写入脚本设置项 closed_time，作为脚本的停止时间
	from datetime import datetime
	obs.obs_data_set_string(settings, 'closed_time', datetime.now().ctime())

def script_defaults(settings):
	# 将设置项 hours 的默认值设置为 3
	obs.obs_data_set_default_int(settings, 'hours', 3)

# def script_tick(seconds):
# 	obs.script_log(obs.LOG_INFO, f'{seconds} OBS 就要无法响应了！！！')