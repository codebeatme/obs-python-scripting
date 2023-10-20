'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/script-function-exports/add-script-properties/ 如何添加腳本屬性
'''

# 匯入模組 obspython
import obspython as obs


def script_properties():
    # 函式 script_properties 用於提供腳本屬性
    # 建立一個表示屬性集的物件
    props = obs.obs_properties_create()

    # 添加文字方塊，其對應的腳本設定項名稱為 message
    obs.obs_properties_add_text(props, 'message', '訊息：', obs.OBS_TEXT_DEFAULT)
    # 添加按鈕，其對應的腳本設定項名稱為 output，點選按鈕將呼叫函式 output_clicked
    obs.obs_properties_add_button(props, 'output', '輸出到日誌', output_clicked)

    return props


def output_clicked(props, prop):
    # 當按鈕被點選時，取得 message 設定項，並在指令稿記錄中顯示
    message = obs.obs_data_get_string(data, 'message')
    obs.script_log(obs.LOG_INFO, message)


# 在模組中定義變數 data，用來表示腳本的設定
data = None

def script_load(settings):
    global data
    # 在腳本載入時，將腳本設定指派給 data
    data = settings
