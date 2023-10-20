'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/script-properties/editable-list/ 如何使用可編輯清單方塊
'''

# 匯入模組 obspython，random
import obspython as obs
import random


def script_properties():
    props = obs.obs_properties_create()

    # 添加一個表示色彩的可編輯清單方塊
    obs.obs_properties_add_editable_list(props, 'colors', '色彩：', obs.OBS_EDITABLE_LIST_TYPE_STRINGS, None, None)

    # 增加一個隨機選擇色彩的按鈕
    obs.obs_properties_add_button(props, 'select_color', '選擇色彩', select_color_clicked)

    return props


# 用於儲存腳本設定
data = None


def script_load(settings):
    # 在腳本載入時，將腳本設定儲存在模組變數 data 中
    global data
    data = settings


def select_color_clicked(props, prop):
    # 隨機的選擇一個色彩，並顯示在指令稿記錄視窗中

    # 取得所有的色彩
    items = obs.obs_data_get_array(data, 'colors')
    # 取得色彩的數量
    count = obs.obs_data_array_count(items)

    # 隨機的選擇一個色彩，並取得色彩的值
    index = random.randint(0, count - 1)
    item = obs.obs_data_array_item(items, index)
    color = obs.obs_data_get_string(item, 'value')

    obs.script_log(obs.LOG_INFO, f'選擇了色彩：{color}')
