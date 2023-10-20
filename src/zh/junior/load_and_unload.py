'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/script-function-exports/script-loading-and-unloading/ 脚本加载，脚本卸载
'''

# 导入模块 obspython，datetime
import obspython as obs
import datetime

# 在模块中定义变量 data，用来表示脚本的设置
data = None

def script_load(settings):
    # 函数 script_load 在脚本加载时被调用
    global data
    # 将脚本设置赋值给 data
    data = settings

    # 读取设置项 last_time，他表示上一次脚本卸载的时间
    last_time = obs.obs_data_get_string(data, 'last_time')

    if last_time:
        obs.script_log(obs.LOG_INFO, f'上一次卸载脚本的时间为：{last_time}')
    else:
        obs.script_log(obs.LOG_INFO, '这是脚本第一次运行！')
    

def script_unload():
    # 函数 script_unload 在脚本卸载时被调用
    # 将当前时间写入设置项 last_time，作为脚本的卸载时间
    last_time = datetime.datetime.now().ctime()
    obs.obs_data_set_string(data, 'last_time', last_time)

    obs.script_log(obs.LOG_INFO, f'卸载脚本：{last_time}')
