'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/script-function-exports/script-updating-and-saving/ 脚本更新，脚本保存
'''

# 导入模块 obspython，datetime
import obspython as obs
import datetime

def script_save(settings):
    # 函数 script_save 在脚本保存时被调用，一般发生在 OBS 关闭时
    # 将当前的时间记录为 OBS 的关闭时间
    closed_time = datetime.datetime.now().ctime()
    obs.obs_data_set_string(settings, 'closed_time', closed_time)

def script_load(settings):
    # 读取脚本设置项 closed_time，并显示为 OBS 的关闭时间
    closed_time = obs.obs_data_get_string(settings, 'closed_time')

    if closed_time:
        obs.script_log(obs.LOG_INFO, f'上一次 OBS 关闭的时间为：{closed_time}')
