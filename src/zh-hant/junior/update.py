'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/script-function-exports/script-updating-and-saving/ 腳本更新，腳本儲存
'''

# 匯入模組 obspython
import obspython as obs


def script_properties():
    # 添加一個表示小時的微調方塊
    props = obs.obs_properties_create()
    obs.obs_properties_add_int(props, 'hours', '小時：', 2, 5, 1)

    return props


def script_update(settings):
    # 函式 script_update 會在腳本更新時被呼叫
    # 讀取腳本設定項 hours 並顯示
    hours = obs.obs_data_get_int(settings, 'hours')
    obs.script_log(obs.LOG_INFO, f'小時更新為：{hours}')
