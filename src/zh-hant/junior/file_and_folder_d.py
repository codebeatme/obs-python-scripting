'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/script-properties/file-and-folder-dialog/ 如何使用檔案對話方塊，資料夾對話方塊
'''

# 匯入模組 obspython
import obspython as obs

def script_properties():
    props = obs.obs_properties_create()

    # 添加一個表示公告資訊的多行文字方塊
    obs.obs_properties_add_text(props, 'announcement', '公告：', obs.OBS_TEXT_MULTILINE)
    # 添加一個選擇公告檔案的對話方塊
    obs.obs_properties_add_path(props, 'path', '公告路徑：', obs.OBS_PATH_FILE, '文字檔案(*.txt)', None)

    # 添加用於載入和儲存公告的按鈕
    obs.obs_properties_add_button(props, 'load', '載入', load_clicked)
    obs.obs_properties_add_button(props, 'save', '儲存', save_clicked)

    return props

# 用於儲存腳本設定
data = None

def script_load(settings):
    # 在腳本載入時，將腳本設定儲存在模組變數 data 中
    global data
    data = settings

def load_clicked(props, prop):
    # 從檔案載入公告資訊並顯示在多行文字方塊中
    path = obs.obs_data_get_string(data, 'path')

    # 如果使用者還沒有指定公告檔案，則無法讀取
    if path:
        # 從檔案讀取公告資訊
        file = open(path, 'r', encoding='utf-8')
        content = file.read()
        file.close()

        # 將公告資訊設定到文字方塊中
        obs.obs_data_set_string(data, 'announcement', content)
        obs.obs_properties_apply_settings(props, data)

    return True


def save_clicked(props, prop):
    # 將多行文字方塊中的內容儲存到公告檔案中
    path = obs.obs_data_get_string(data, 'path')

    # 如果使用者還沒有指定公告檔案，則無法儲存
    if path:
        # 取得多行文字方塊中的公告內容
        content = obs.obs_data_get_string(data, 'announcement')

        # 將公告內容寫入檔案
        file = open(path, 'w', encoding='utf-8')
        file.write(content)
        file.close()
