'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/add-and-remove-script-timers/ 如何添加和移除腳本計時器
'''

# 匯入模組 obspython，datetime
import obspython as obs
import datetime

def show_time():
    # 回呼函式 show_time，可以顯示當前的時間
    time = datetime.datetime.now().ctime()
    obs.script_log(obs.LOG_INFO, f'當前時間：{time}')

# 使用 timer_add 添加計時器
obs.timer_add(show_time, 1000)

class Callback:
    # 類別 Callback，包含回呼的方法，雖然有點不合理

    def show_time_too(self):
        # 方法 show_time_too，同樣顯示當前時間
        time = datetime.datetime.now().ctime()
        obs.script_log(obs.LOG_INFO, f'這裏還有一個時間：{time}')
        obs.remove_current_callback()

# 使用 timer_add 添加計時器
obs.timer_add(Callback().show_time_too, 1000)


def script_properties():
    # 建立一個用於停止顯示時間的按鈕
    props = obs.obs_properties_create()

    # 點選按鈕後，將停止顯示時間
    obs.obs_properties_add_button(props, 'stop', '停止顯示時間', stop_clicked)

    return props


def stop_clicked(props, prop):
    # 停止回呼函式 show_time 對應的計時器
    obs.timer_remove(show_time)
