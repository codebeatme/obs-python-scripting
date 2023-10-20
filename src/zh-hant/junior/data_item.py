'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/data/get-and-set-data-item/ 如何取得和設定資料項
'''

# 匯入模組 obspython
import obspython as obs


def script_properties():
    props = obs.obs_properties_create()

    # 添加一個設定標題內容的文字方塊
    prop = obs.obs_properties_add_text(props, 'title', '標題：', obs.OBS_TEXT_DEFAULT)
    obs.obs_property_set_modified_callback(prop, title_modified)

    return props


def title_modified(props, prop, settings):
    # 取得文字方塊中的內容
    title = obs.obs_data_get_string(settings, 'title')

    # 取得場景中的文字來源
    source = obs.obs_get_source_by_name('Title')

    # 將文字方塊的內容設定到文字來源
    data = obs.obs_data_create()
    obs.obs_data_set_string(data, 'text', title)
    obs.obs_source_update(source, data)

    # 釋放資料物件和來源物件
    obs.obs_data_release(data)
    obs.obs_source_release(source)
