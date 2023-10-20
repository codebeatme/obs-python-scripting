'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/script-properties/check-box/ 如何使用核取方塊
'''

# 匯入模組 obspython
import obspython as obs
import datetime


def script_properties():
    props = obs.obs_properties_create()

    # 添加一個核取方塊，用於確定是否啟用計時器
    obs.obs_properties_add_bool(props, 'enable_timer', '啟用計時器？')

    return props


def script_update(settings):
    # 當腳本更新時，取得核取方塊的選取狀態
    display = obs.obs_data_get_bool(settings, 'enable_timer')

    # 根據核取方塊的選取狀態，添加或移除計時器
    if display:
        # 添加顯示時間的計時器
        obs.timer_add(show_time, 1000)
    else:
        # 移除顯示時間的計時器
        obs.timer_remove(show_time)


def show_time():
    # 回呼函式 show_time，用於在指令稿記錄中顯示時間
    time = datetime.datetime.now().ctime()
    obs.script_log(obs.LOG_INFO, f'當前時間：{time}')
