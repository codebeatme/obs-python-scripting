'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/data/get-and-set-data-item/ 如何获取和设置数据项
'''

# 导入模块 obspython
import obspython as obs


def script_properties():
    props = obs.obs_properties_create()

    # 添加一个设置标题内容的文本框
    prop = obs.obs_properties_add_text(props, 'title', '标题：', obs.OBS_TEXT_DEFAULT)
    obs.obs_property_set_modified_callback(prop, title_modified)

    return props


def title_modified(props, prop, settings):
    # 获取文本框中的内容
    title = obs.obs_data_get_string(settings, 'title')

    # 获取场景中的文本源
    source = obs.obs_get_source_by_name('Title')

    # 将文本框的内容设置到文本源
    data = obs.obs_data_create()
    obs.obs_data_set_string(data, 'text', title)
    obs.obs_source_update(source, data)

    # 释放数据对象和源对象
    obs.obs_data_release(data)
    obs.obs_source_release(source)
