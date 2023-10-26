'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/data/get-and-set-data-item-default-value/ 如何取得和設定資料項的預設值
'''

# 匯入模組 obspython
import obspython as obs


# 用於儲存腳本設定
data = None


def script_load(settings):
    # 在腳本載入時，將腳本設定儲存在模組變數 data 中
    global data
    data = settings


def script_properties():
    props = obs.obs_properties_create()

    # 添加設定訊息內容的文字方塊
    obs.obs_properties_add_text(props, 'message', '訊息：', obs.OBS_TEXT_DEFAULT)

    # 添加選擇延遲時間的下拉式方塊
    prop = obs.obs_properties_add_list(props, 'time', '延遲時間：', obs.OBS_COMBO_TYPE_LIST, obs.OBS_COMBO_FORMAT_STRING)
    obs.obs_property_list_add_string(prop, '長', 'long')
    obs.obs_property_list_add_string(prop, '短', 'short')

    # 添加一個顯示訊息的按鈕
    obs.obs_properties_add_button(props, 'show', '顯示', show_clicked)

    return props


def script_defaults(settings):
    # 為腳本設定項設定預設值，包括預設訊息和延遲時間
    obs.obs_data_set_default_string(settings, 'message', '這是預設訊息')
    obs.obs_data_set_default_string(settings, 'time', 'short')


def show_clicked(props, prop):
    # 根據使用者選擇的延遲時間，決定延遲的秒數
    time = obs.obs_data_get_string(data, 'time')
    seconds = None

    if time == 'long':
        seconds = 3
    elif time == 'short':
        seconds = 1

    if seconds:
        # 添加計時器，時間間隔為指定的秒數
        obs.timer_add(log, 1000 * seconds)
        obs.script_log(obs.LOG_INFO, f'{seconds} 秒後顯示訊息')


def log():
    message = obs.obs_data_get_string(data, 'message')
    obs.script_log(obs.LOG_INFO, message)

    # 移除之前添加的計時器
    obs.remove_current_callback()

