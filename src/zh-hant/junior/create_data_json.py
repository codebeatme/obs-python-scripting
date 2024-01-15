'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/data/create-data-from-json/ 如何從 JSON 建立資料
'''

# 匯入模組 obspython，json
import obspython as obs
import json

def script_properties():
    props = obs.obs_properties_create()

    # 添加一個表示透明度的滑桿
    prop = obs.obs_properties_add_float_slider(props, 'opacity', '透明度：', 0, 100, 10)
    obs.obs_property_set_modified_callback(prop, opacity_modified)

    return props

def opacity_modified(props, prop, settings):
    # 取得透明度
    opacity = obs.obs_data_get_double(settings, 'opacity')

    # 取得場景中的文字來源 Welcome
    source = obs.obs_get_source_by_name('Welcome')

    # 建置一個 JSON 字串
    json_string = json.dumps({ "opacity": opacity })
    # 將建置的 JSON 字串轉換為資料物件
    data = obs.obs_data_create_from_json(json_string)

    # 將資料物件應用至文字來源
    obs.obs_source_update(source, data)

    # 釋放資料物件和來源物件
    obs.obs_data_release(data)
    obs.obs_source_release(source)
