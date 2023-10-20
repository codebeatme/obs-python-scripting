'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/script-properties/color-dialog/ 如何使用色彩對話方塊
'''

# 匯入模組 obspython
import obspython as obs

def script_properties():
    props = obs.obs_properties_create()

    # 添加一個色彩對話方塊
    prop = obs.obs_properties_add_color(props, 'text_color', '色彩：')
    obs.obs_property_set_modified_callback(prop, color_modified)

    return props

def color_modified(props, prop, settings):
    # 取得色彩對話方塊所確定的色彩
    text_color = obs.obs_data_get_int(settings, 'text_color')

    # 取得場景中的文字來源 Welcome
    source = obs.obs_get_source_by_name('Welcome')

    # 將色彩對話方塊的色彩應用到文字來源
    data = obs.obs_data_create()
    obs.obs_data_set_int(data, 'color', text_color)
    obs.obs_source_update(source, data)

    # 釋放資料物件和來源物件
    obs.obs_data_release(data)
    obs.obs_source_release(source)
