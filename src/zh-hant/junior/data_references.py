'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/data/add-and-release-data-reference/ 如何添加和釋放資料參考
'''

# 匯入模組 obspython
import obspython as obs

# 一個資料物件
data = None


def script_properties():
    global data
    props = obs.obs_properties_create()

    # 建立一個資料物件，包含了姓名和年齡
    data = obs.obs_data_create()
    obs.obs_data_set_string(data, 'name', '保密的哦！')
    obs.obs_data_set_int(data, 'age', 77)

    # 為資料物件添加新的參考，將需要呼叫兩次 obs_data_release
    obs.obs_data_addref(data)

    # 添加顯示姓名和年齡的按鈕
    obs.obs_properties_add_button(props, 'show_name', '顯示姓名', show_name_clicked)
    obs.obs_properties_add_button(props, 'show_age', '顯示年齡', show_age_clicked)

    return props


def show_name_clicked(props, prop):
    # 顯示姓名，然後釋放對資料物件的一個參考
    name = obs.obs_data_get_string(data, 'name')
    obs.script_log(obs.LOG_INFO, f'姓名：{name}')
    # 釋放資料物件
    obs.obs_data_release(data)


def show_age_clicked(props, prop):
    # 顯示年齡，然後釋放對資料物件的一個參考
    age = obs.obs_data_get_int(data, 'age')
    obs.script_log(obs.LOG_INFO, f'年齡：{age}')
    # 釋放資料物件
    obs.obs_data_release(data)
