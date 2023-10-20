'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/script-properties/general-control-functions/ 通用控製項函式有哪些
'''

# 匯入模組 obspython
import obspython as obs

def script_properties():
    props = obs.obs_properties_create()

    # 添加一個按鈕，用於確定一些串流的設定
    obs.obs_properties_add_button(props, 'ok', '確定', ok_clicked)

    # 添加一個核取方塊，表示串流是否顯示歡迎訊息
    prop = obs.obs_properties_add_bool(props, 'display_welcome', '是否顯示歡迎訊息？')
    obs.obs_property_set_modified_callback(prop, display_welcome_modified)

    # 添加一個文字方塊，表示歡迎訊息
    prop = obs.obs_properties_add_text(props, 'welcome', '歡迎訊息：', obs.OBS_TEXT_DEFAULT)
    # 設定文字方塊不顯示
    obs.obs_property_set_visible(prop, False)

    return props

def ok_clicked(props, prop):
    # 確定按鈕不能被再一次的點選
    obs.obs_property_set_enabled(prop, False)

    # 如果文字方塊可見，則認為顯示歡迎訊息
    prop_welcome = obs.obs_properties_get(props, 'welcome')
    obs.script_log(obs.LOG_INFO, f'顯示歡迎訊息？{obs.obs_property_visible(prop_welcome)}')
    return True

def display_welcome_modified(props, prop, settings):
    # 點選核取方塊時，切換文字方塊的可見狀態
    # 取得文字方塊
    prop_welcome = obs.obs_properties_get(props, 'welcome')

    # 取得並反轉文字方塊的可見狀態
    visible = not obs.obs_property_visible(prop_welcome)
    obs.obs_property_set_visible(prop_welcome, visible)
    return True
