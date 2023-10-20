'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/script-properties/combo-box/ 如何使用下拉式方塊
'''

# 匯入模組 obspython
import obspython as obs

def script_properties():
    props = obs.obs_properties_create()

    # 添加一個表示串流平臺的下拉式方塊
    prop = obs.obs_properties_add_list(props, 'platform', '串流平臺：', obs.OBS_COMBO_TYPE_LIST, obs.OBS_COMBO_FORMAT_STRING)

    # 為下拉式方塊添加項
    obs.obs_property_list_add_string(prop, 'YouTube', 'yt')
    obs.obs_property_list_add_string(prop, 'Twitch', 't')
    # 在下拉式方塊的第二個位置插入項，並使該項不可用
    obs.obs_property_list_insert_string(prop, 1, 'Unkown', 'u')
    obs.obs_property_list_item_disable(prop, 1, True)

    # 增加一個開始串流的按鈕
    obs.obs_properties_add_button(props, 'start', '開始串流', start_clicked)

    return props

# 用於儲存腳本設定
data = None

def script_load(settings):
    # 在腳本載入時，將腳本設定儲存在模組變數 data 中
    global data
    data = settings

def start_clicked(props, prop):
    # 取得下拉式方塊中選取的項，並顯示在指令稿記錄視窗中
    platform = obs.obs_data_get_string(data, 'platform')

    obs.script_log(obs.LOG_INFO, f'開始在 {platform} 串流')