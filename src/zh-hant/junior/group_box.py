'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/script-properties/group-box/ 如何使用群組方塊
'''

# 匯入模組 obspython
import obspython as obs

def script_properties():
    props = obs.obs_properties_create()

    # 建立登入群組方塊對應的屬性集
    login_props = obs.obs_properties_create()
    # 添加登入群組方塊
    obs.obs_properties_add_group(props, 'group_login', '使用者登入', obs.OBS_GROUP_NORMAL, login_props)

    # 為登入群組方塊添加文字方塊和按鈕
    obs.obs_properties_add_text(login_props, 'user_name', '使用者名稱：', obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_text(login_props, 'password', '密碼：', obs.OBS_TEXT_PASSWORD)
    obs.obs_properties_add_button(login_props, 'login', '登入', login_clicked)

    # 添加一個用來在成功登入後顯示的文字方塊，登入前並不顯示
    prop_welcome = obs.obs_properties_add_text(props, 'welcome', '歡迎：', obs.OBS_TEXT_INFO)
    obs.obs_property_set_visible(prop_welcome, False)

    return props


# 用於儲存腳本設定
data = None


def script_load(settings):
    # 在腳本載入時，將腳本設定儲存在模組變數 data 中
    global data
    data = settings

def login_clicked(props, prop):
    # 取得使用者輸入的使用者名稱和密碼
    user_name = obs.obs_data_get_string(data, 'user_name')
    password = obs.obs_data_get_string(data, 'password')

    # 簡單的判斷登入資訊，登入成功則執行一些作業
    if user_name == 'hero' and password == '123':
        # 隱藏登入群組方塊
        prop_group = obs.obs_properties_get(props, 'group_login')
        obs.obs_property_set_visible(prop_group, False)

        # 使 welcome 文字方塊可見，並展示使用者名稱
        prop_welcome = obs.obs_properties_get(props, 'welcome')
        obs.obs_data_set_string(data, 'welcome', f'使用者 {user_name}')
        obs.obs_properties_apply_settings(props, data)
        obs.obs_property_set_visible(prop_welcome, True)

    return True