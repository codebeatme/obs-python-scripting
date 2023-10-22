'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/data/get-json-from-data/ 如何从数据获取 JSON
'''

# 导入模块 obspython，json
import obspython as obs
import json

def script_properties():
    props = obs.obs_properties_create()

    # 添加一个表示透明度的滑块
    prop = obs.obs_properties_add_float_slider(props, 'opacity', '透明度：', 0, 100, 10)
    obs.obs_property_set_modified_callback(prop, opacity_modified)

    return props

def opacity_modified(props, prop, settings):
    # 获取透明度
    opacity = obs.obs_data_get_double(settings, 'opacity')

    # 获取场景中的文本源 Welcome
    source = obs.obs_get_source_by_name('Welcome')

    # 生成一个 JSON 字符串
    json_string = json.dumps({ "opacity": opacity })
    # 将生成的 JSON 字符串转换为数据对象
    data = obs.obs_data_create_from_json(json_string)

    # 将数据对象应用至文本源
    obs.obs_source_update(source, data)

    # 释放数据对象和源对象
    obs.obs_data_release(data)
    obs.obs_source_release(source)
