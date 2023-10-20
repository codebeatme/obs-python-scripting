'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/script-function-exports/script-loading-and-unloading/ 腳本載入，腳本卸載
'''

# 匯入模組 obspython，datetime
import obspython as obs
import datetime

# 在模組中定義變數 data，用來表示腳本的設定
data = None

def script_load(settings):
    # 函式 script_load 在腳本載入時被呼叫
    global data
    # 將腳本設定指派給 data
    data = settings

    # 讀取設定項 last_time，他表示上一次腳本卸載的時間
    last_time = obs.obs_data_get_string(data, 'last_time')

    if last_time:
        obs.script_log(obs.LOG_INFO, f'上一次卸載腳本的時間為：{last_time}')
    else:
        obs.script_log(obs.LOG_INFO, '這是腳本第一次執行！')
    

def script_unload():
    # 函式 script_unload 在腳本卸載時被呼叫
    # 將當前時間寫入設定項 last_time，作為腳本的卸載時間
    last_time = datetime.datetime.now().ctime()
    obs.obs_data_set_string(data, 'last_time', last_time)

    obs.script_log(obs.LOG_INFO, f'卸載腳本：{last_time}')
