'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/script-function-exports/set-script-setting-default-values/ 如何設定腳本設定的預設值
'''

# 匯入模組 obspython
import obspython as obs

def script_properties():
    # 添加一個控製是否自動執行的核取方塊
    props = obs.obs_properties_create()
    obs.obs_properties_add_bool(props, 'autorun', '自動執行')

    return props

def script_defaults(settings):
    # 函式 script_defaults 用於設定腳本設定的預設值
    # 將設定項 autorun 的預設值設定為 True
    obs.obs_data_set_default_bool(settings, 'autorun', True)

def script_load(settings):
    # 在腳本載入時，讀取設定項 autorun
    autorun = obs.obs_data_get_bool(settings, 'autorun')

    # 如果是自動執行，則輸出一段文字資訊
    if autorun:
        obs.script_log(obs.LOG_INFO, '自動執行已經開啟')
