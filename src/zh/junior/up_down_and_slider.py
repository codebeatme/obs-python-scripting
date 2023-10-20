'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/script-properties/numeric-up-down-and-slider/ 如何使用数字显示框，滑块
'''

# 导入模块 obspython，datetime
import obspython as obs
import datetime

seconds = 0

def script_properties():
    props = obs.obs_properties_create()

    # 添加一个滑块，用来设置计时器的时间间隔
    p = obs.obs_properties_add_int_slider(props, 'seconds', '时间间隔（秒）', 1, 5, 1)

    # 添加一个按钮，用来启动计时器
    obs.obs_properties_add_button(props, 'begin', '开始', begin_clicked)

    t = obs.obs_property_int_type(p)
    obs.script_log(obs.LOG_INFO, f'{t} {obs.OBS_NUMBER_SCROLLER} {obs.OBS_NUMBER_SLIDER}')

    return props

def script_update(settings):
    # 当脚本更新时，获取滑块中的秒数
    global seconds
    seconds = obs.obs_data_get_int(settings, 'seconds')

def begin_clicked(props, prop):

    # 如果滑块从未被调整过，则 seconds 是 0
    if seconds:
        # 添加显示时间的计时器
        obs.timer_add(show_time, seconds * 1000)
        # 将按钮设置为不可用
        obs.obs_property_set_enabled(prop, False)

    return True


def show_time():
    # 回调函数 show_time，用于在脚本日志中显示时间
    time = datetime.datetime.now().ctime()
    obs.script_log(obs.LOG_INFO, f'当前时间：{time}')
