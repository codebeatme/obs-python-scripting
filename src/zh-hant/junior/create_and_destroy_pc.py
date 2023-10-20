'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/script-properties/create-and-destroy-property-collections/ 如何建立和終結屬性集
'''

# 匯入模組 obspython，datetime
import obspython as obs
import datetime

# 開始時間
start = None

def script_properties():
    # script_properties 傳回一個屬性集物件
    # 呼叫 obs_properties_create 函式建立屬性集
    props = obs.obs_properties_create()

    # 添加一個判斷是否可以結束串流的按鈕
    obs.obs_properties_add_button(props, 'over', '結束了？', over_clicked)

    # 將當前時間記錄為開始時間
    global start
    start = datetime.datetime.now()

    return props

def over_clicked(props, prop):
    # 當按鈕被點選時，判斷是否可以結束串流

    # 計算從開始時間到現在經歷的秒數
    end = datetime.datetime.now()
    seconds = (end - start).total_seconds()

    # 已經過了 1 分鐘，則顯示可以結束
    if seconds > 60:
        obs.script_log(obs.LOG_INFO, '可以結束了')
    else:
        obs.script_log(obs.LOG_INFO, '串流還不到 1 分鐘')
