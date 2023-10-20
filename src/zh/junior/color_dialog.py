'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/script-properties/color-dialog/ 如何使用颜色对话框
'''

# 导入模块 obspython
import obspython as obs

def script_properties():
    props = obs.obs_properties_create()

    # 添加一个颜色对话框
    prop = obs.obs_properties_add_color(props, 'text_color', '颜色：')
    obs.obs_property_set_modified_callback(prop, color_modified)

    return props

def color_modified(props, prop, settings):
    # 获取颜色对话框所确定的颜色
    text_color = obs.obs_data_get_int(settings, 'text_color')

    # 获取场景中的文本源 Welcome
    source = obs.obs_get_source_by_name('Welcome')

    # 将颜色对话框的颜色应用到文本源
    data = obs.obs_data_create()
    obs.obs_data_set_int(data, 'color', text_color)
    obs.obs_source_update(source, data)

    # 释放数据对象和源对象
    obs.obs_data_release(data)
    obs.obs_source_release(source)
