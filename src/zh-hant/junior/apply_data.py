'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/data/apply-data-to-target/ 如何應用資料至目標
'''

# 匯入模組 obspython
import obspython as obs

def script_properties():
    props = obs.obs_properties_create()

    # 添加合併樣式檔案的對話方塊
    obs.obs_properties_add_button(props, 'style', '合併樣式', style_clicked)

    return props

def style_clicked(props, prop):
    data = obs.obs_data_create()
    # 從檔案 white.json 載入白色樣式
    data_white = obs.obs_data_create_from_json_file('white.json')

    # 將包含白色樣式的資料物件合併至 data
    obs.obs_data_apply(data, data_white)
    # 輸出 data 對應的 JSON 字串
    json_string = obs.obs_data_get_json(data)
    obs.script_log(obs.LOG_INFO, json_string)

    # 從檔案 black.json 載入黑色樣式
    data_black = obs.obs_data_create_from_json_file('black.json')

    # 將包含黑色樣式的資料物件合併至 data
    obs.obs_data_apply(data, data_black)
    # 輸出 data 對應的 JSON 字串
    json_string = obs.obs_data_get_json(data)
    obs.script_log(obs.LOG_INFO, json_string)

    # 取得場景中的文字來源 Welcome
    source = obs.obs_get_source_by_name('Welcome')
    # 將樣式應用到文字來源
    obs.obs_source_update(source, data)

    # 釋放資料物件和來源物件
    obs.obs_data_release(data_black)
    obs.obs_data_release(data_white)
    obs.obs_data_release(data)
    obs.obs_source_release(source)
