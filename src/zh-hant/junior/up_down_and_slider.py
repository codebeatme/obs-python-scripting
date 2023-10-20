'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/script-properties/numeric-up-down-and-slider/ 如何使用微調方塊，滑桿
'''

# 匯入模組 obspython，datetime
import obspython as obs
import datetime

seconds = 0

def script_properties():
    props = obs.obs_properties_create()

    # 添加一個滑桿，用來設定計時器的時間間隔
    p = obs.obs_properties_add_int_slider(props, 'seconds', '時間間隔（秒）', 1, 5, 1)

    # 添加一個按鈕，用來啟動計時器
    obs.obs_properties_add_button(props, 'begin', '開始', begin_clicked)

    t = obs.obs_property_int_type(p)
    obs.script_log(obs.LOG_INFO, f'{t} {obs.OBS_NUMBER_SCROLLER} {obs.OBS_NUMBER_SLIDER}')

    return props

def script_update(settings):
    # 當腳本更新時，取得滑桿中的秒數
    global seconds
    seconds = obs.obs_data_get_int(settings, 'seconds')

def begin_clicked(props, prop):

    # 如果滑桿從未被調整過，則 seconds 是 0
    if seconds:
        # 添加顯示時間的計時器
        obs.timer_add(show_time, seconds * 1000)
        # 將按鈕設定為不可用
        obs.obs_property_set_enabled(prop, False)

    return True


def show_time():
    # 回呼函式 show_time，用於在指令稿記錄中顯示時間
    time = datetime.datetime.now().ctime()
    obs.script_log(obs.LOG_INFO, f'當前時間：{time}')
