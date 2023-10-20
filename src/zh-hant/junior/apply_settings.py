'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/script-properties/apply-settings-to-property-collection/ 如何套用設定至屬性集
'''

# 匯入模組 obspython，random
import obspython as obs
import random

# 用於儲存腳本設定
data = None
# 一組可供選擇的訊息
messages = ('天氣不錯！', '吃了嗎？', '下雨啦！')


def script_load(settings):
    # 在腳本載入時，將腳本設定儲存在模組變數 data 中
    global data
    data = settings


def script_properties():
    props = obs.obs_properties_create()

    # 添加一個文字方塊和按鈕
    obs.obs_properties_add_text(props, 'message', '訊息：', obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_button(props, 'random_message', '隨機訊息', random_message_clicked)

    return props


def random_message_clicked(props, prop):
    # 隨機的取得一個訊息
    message = messages[random.randint(0, 2)]

    # 將訊息寫入腳本設定項 message
    obs.obs_data_set_string(data, 'message', message)
    # 將腳本設定套用到腳本屬性集
    obs.obs_properties_apply_settings(props, data)
    return True
