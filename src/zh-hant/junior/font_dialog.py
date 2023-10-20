'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/script-properties/font-dialog/ 如何使用字型對話方塊
'''

# 匯入模組 obspython
import obspython as obs

def script_properties():
    props = obs.obs_properties_create()

    # 添加一個字型對話方塊
    prop = obs.obs_properties_add_font(props, 'text_font', '字型：')
    obs.obs_property_set_modified_callback(prop, font_modified)

    return props

def font_modified(props, prop, settings):
    # 取得字型對話方塊所確定的字型
    text_font = obs.obs_data_get_obj(settings, 'text_font')

    # 取得場景中的文字來源 Welcome
    source = obs.obs_get_source_by_name('Welcome')

    # 將字型對話方塊的字型應用到文字來源
    data = obs.obs_data_create()
    obs.obs_data_set_obj(data, 'font', text_font)
    obs.obs_source_update(source, data)

    # 釋放資料物件和來源物件
    obs.obs_data_release(text_font)
    obs.obs_data_release(data)
    obs.obs_source_release(source)
