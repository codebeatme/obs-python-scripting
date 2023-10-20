'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/script-function-exports/script-updating-and-saving/ 腳本更新，腳本儲存
'''

# 匯入模組 obspython，datetime
import obspython as obs
import datetime

def script_save(settings):
    # 函式 script_save 在腳本儲存時被呼叫，一般發生在 OBS 關閉時
    # 將當前的時間記錄為 OBS 的關閉時間
    closed_time = datetime.datetime.now().ctime()
    obs.obs_data_set_string(settings, 'closed_time', closed_time)

def script_load(settings):
    # 讀取腳本設定項 closed_time，並顯示為 OBS 的關閉時間
    closed_time = obs.obs_data_get_string(settings, 'closed_time')

    if closed_time:
        obs.script_log(obs.LOG_INFO, f'上一次 OBS 關閉的時間為：{closed_time}')
