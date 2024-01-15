'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/data/get-json-from-data/ 如何從資料取得 JSON
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

    # 添加設定項 message
    obs.obs_data_set_string(data, 'message', '你好！')

    # 添加兩個按鈕
    obs.obs_properties_add_button(props, 'json', '取得設定的 JSON', json_clicked)
    obs.obs_properties_add_button(props, 'last_json', '最後的 JSON', last_json_clicked)

    return props

def json_clicked(props, prop):
    # 取得腳本設定對應的 JSON 字串
    json_string = obs.obs_data_get_json(data)
    obs.script_log(obs.LOG_INFO, f'設定的 JSON：{json_string}')

    # 修改設定項 message
    obs.obs_data_set_string(data, 'message', '再見！')


def last_json_clicked(props, prop):
    # 取得上一次腳本設定建置的 JSON 字串
    json_string = obs.obs_data_get_last_json(data)
    obs.script_log(obs.LOG_INFO, f'最後的 JSON：{json_string}')
