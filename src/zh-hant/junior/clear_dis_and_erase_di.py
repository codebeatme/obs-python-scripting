'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/data/clear-data-items-and-erase-data-item/ 如何清除所有資料項，抹除資料項
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

    # 添加用於填寫玩家和遊戲資訊的文字方塊
    obs.obs_properties_add_text(props, 'player', '玩家：', obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_text(props, 'game', '遊戲：', obs.OBS_TEXT_DEFAULT)
    # 添加顯示祝賀資訊的文字方塊
    obs.obs_properties_add_text(props, 'done', '祝賀，你已經完成所有步驟！', obs.OBS_TEXT_INFO)
    # 添加下一步和重置按鈕
    obs.obs_properties_add_button(props, 'next', '下一步', next_clicked)
    obs.obs_properties_add_button(props, 'reset', '重置', reset_clicked)

    # 刷新介面，用於顯示或隱藏文字方塊和按鈕
    refresh_ui(props)

    return props

def next_clicked(props, prop):
    # 當下一步按鈕被點選時，將腳本設定項 step 加 1，表示進入下一步
    step = obs.obs_data_get_int(data, 'step')
    obs.obs_data_set_int(data, 'step', step + 1)

    # 刷新介面，切換顯示下一步所用的控製項
    refresh_ui(props)
    return True

def reset_clicked(props, prop):
    # 清空所有的腳本設定項
    obs.obs_data_clear(data)
    # 需要將腳本設定應用到屬性，否則文字方塊中的已有內容不會被清空
    obs.obs_properties_apply_settings(props, data)

    # 刷新介面，恢復到第一步
    refresh_ui(props)
    return True

def refresh_ui(props):
    # 腳本設定項 step 表示當前是第幾步
    step = obs.obs_data_get_int(data, 'step')

    # 根據 step 來決定哪些文字方塊和按鈕需要顯示
    prop = obs.obs_properties_get(props, 'player')
    obs.obs_property_set_visible(prop, step == 0)

    prop = obs.obs_properties_get(props, 'game')
    obs.obs_property_set_visible(prop, step == 1)

    prop = obs.obs_properties_get(props, 'done')
    obs.obs_property_set_visible(prop, step == 2)

    prop = obs.obs_properties_get(props, 'next')
    obs.obs_property_set_visible(prop, step != 2)

    prop = obs.obs_properties_get(props, 'reset')
    obs.obs_property_set_visible(prop, step == 2)