'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/data/create-data/ 如何建立資料
'''

# 匯入模組 obspython
import obspython as obs

def script_properties():
    props = obs.obs_properties_create()

    # 添加一個選擇背景圖片的檔案對話方塊
    prop = obs.obs_properties_add_path(props, 'path', '圖片路徑：', obs.OBS_PATH_FILE, '圖片檔案(*.jpg *.png)', None)
    obs.obs_property_set_modified_callback(prop, path_modified)

    return props

def path_modified(props, prop, settings):
    # 讀取檔案對話方塊確定的檔案
    path = obs.obs_data_get_string(settings, 'path')

    # 如果使用者還沒有選擇任何圖片，則不設定圖片來源
    if path:
        # 取得場景中的圖片來源
        source = obs.obs_get_source_by_name('bg')

        # 將圖片檔案路徑設定到圖片來源
        data = obs.obs_data_create()
        obs.obs_data_set_string(data, 'file', path)
        obs.obs_source_update(source, data)

        # 釋放資料物件和來源物件
        obs.obs_data_release(data)
        obs.obs_source_release(source)
