'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/script-properties/button/ 如何使用按鈕
'''

# 匯入模組 obspython
import obspython as obs

def script_properties():
    props = obs.obs_properties_create()

    # 添加一個按鈕
    prop = obs.obs_properties_add_button(props, 'output', '輸出', output_clicked)
    # 設定按鈕的類型和 URL，回呼函式 output_clicked 將失效
    obs.obs_property_button_set_type(prop, obs.OBS_BUTTON_URL)
    obs.obs_property_button_set_url(prop, 'http://www.bing.com/')

    return props

def output_clicked(props, prop):
    # 取得按鈕的 URL，並輸出到指令稿記錄視窗中，但這不會發生
    url = obs.obs_property_button_url(prop)
    obs.script_log(obs.LOG_INFO, f'按鈕 URL：{url}')