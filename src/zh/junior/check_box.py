'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/script-properties/check-box/ 如何使用复选框
'''

# 导入模块 obspython
import obspython as obs
import datetime


def script_properties():
    props = obs.obs_properties_create()

    # 添加一个复选框，用于确定是否启用计时器
    obs.obs_properties_add_bool(props, 'enable_timer', '启用计时器？')

    return props


def script_update(settings):
    # 当脚本更新时，获取复选框的选中状态
    display = obs.obs_data_get_bool(settings, 'enable_timer')

    # 根据复选框的选中状态，添加或移除计时器
    if display:
        # 添加显示时间的计时器
        obs.timer_add(show_time, 1000)
    else:
        # 移除显示时间的计时器
        obs.timer_remove(show_time)


def show_time():
    # 回调函数 show_time，用于在脚本日志中显示时间
    time = datetime.datetime.now().ctime()
    obs.script_log(obs.LOG_INFO, f'当前时间：{time}')
