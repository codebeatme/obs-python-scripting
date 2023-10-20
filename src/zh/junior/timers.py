'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/add-and-remove-script-timers/ 如何添加和移除脚本计时器
'''

# 导入模块 obspython，datetime
import obspython as obs
import datetime

def show_time():
    # 回调函数 show_time，可以显示当前的时间
    time = datetime.datetime.now().ctime()
    obs.script_log(obs.LOG_INFO, f'当前时间：{time}')

# 使用 timer_add 添加计时器
obs.timer_add(show_time, 1000)

class Callback:
    # 类 Callback，包含回调的方法，虽然有点不合理

    def show_time_too(self):
        # 方法 show_time_too，同样显示当前时间
        time = datetime.datetime.now().ctime()
        obs.script_log(obs.LOG_INFO, f'这里还有一个时间：{time}')
        obs.remove_current_callback()

# 使用 timer_add 添加计时器
obs.timer_add(Callback().show_time_too, 1000)


def script_properties():
    # 创建一个用于停止显示时间的按钮
    props = obs.obs_properties_create()

    # 点击按钮后，将停止显示时间
    obs.obs_properties_add_button(props, 'stop', '停止显示时间', stop_clicked)

    return props


def stop_clicked(props, prop):
    # 停止回调函数 show_time 对应的计时器
    obs.timer_remove(show_time)
