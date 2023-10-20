'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/script-properties/text-box/ 如何使用文字方塊
'''

# 匯入模組 obspython
import obspython as obs


def script_properties():
    props = obs.obs_properties_create()

    # 添加一個表示使用者名稱的文字方塊
    obs.obs_properties_add_text(props, 'user_name', '使用者名稱：', obs.OBS_TEXT_DEFAULT)
    # 添加一個表示密碼的文字方塊
    obs.obs_properties_add_text(props, 'password', '密碼：', obs.OBS_TEXT_PASSWORD)

    # 添加一個唯讀的文字方塊，用於顯示登入的結果
    obs.obs_properties_add_text(props, 'info', '結果：', obs.OBS_TEXT_INFO)
    # 清除上一次顯示的登入結果
    set_info(props, '', obs.OBS_TEXT_INFO_NORMAL)

    # 添加一個用於登入的按鈕
    obs.obs_properties_add_button(props, 'login', '登入', login_clicked)

    return props


# 用於儲存腳本設定
data = None


def script_load(settings):
    # 在腳本載入時，將腳本設定儲存在模組變數 data 中
    global data
    data = settings


def set_info(props, content, type):
    # 設定唯讀文字方塊所顯示的內容
    obs.obs_data_set_string(data, 'info', content)
    obs.obs_properties_apply_settings(props, data)

    # 設定唯讀文字方塊的資訊類型
    prop = obs.obs_properties_get(props, 'info')
    obs.obs_property_text_set_info_type(prop, type)


def login_clicked(props, prop):
    # 登入按鈕被點選時，取得並驗證使用者名稱和密碼
    user_name = obs.obs_data_get_string(data, 'user_name')
    password = obs.obs_data_get_string(data, 'password')

    # 簡單的判斷使用者名稱和密碼，並顯示不同的訊息
    if user_name == 'abc' and password == 'abc':
        set_info(props, '登入成功！', obs.OBS_TEXT_INFO_NORMAL)
    else:
        set_info(props, '使用者名稱或密碼錯誤！', obs.OBS_TEXT_INFO_WARNING)

    return True
