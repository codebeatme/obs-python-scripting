'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/script-properties/font-dialog/ 如何使用字体对话框
'''

# 导入模块 obspython
import obspython as obs

def script_properties():
    props = obs.obs_properties_create()

    # 添加一个字体对话框
    prop = obs.obs_properties_add_font(props, 'text_font', '字体：')
    obs.obs_property_set_modified_callback(prop, font_modified)

    return props

def font_modified(props, prop, settings):
    # 获取字体对话框所确定的字体
    text_font = obs.obs_data_get_obj(settings, 'text_font')

    # 获取场景中的文本源 Welcome
    source = obs.obs_get_source_by_name('Welcome')

    # 将字体对话框的字体应用到文本源
    data = obs.obs_data_create()
    obs.obs_data_set_obj(data, 'font', text_font)
    obs.obs_source_update(source, data)

    # 释放数据对象和源对象
    obs.obs_data_release(text_font)
    obs.obs_data_release(data)
    obs.obs_source_release(source)
