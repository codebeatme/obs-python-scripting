'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/data/apply-data-to-target/ 如何应用数据至目标
'''

# 导入模块 obspython
import obspython as obs

def script_properties():
    props = obs.obs_properties_create()

    # 添加合并样式文件的对话框
    obs.obs_properties_add_button(props, 'style', '合并样式', style_clicked)

    return props

def style_clicked(props, prop):
    data = obs.obs_data_create()
    # 从文件 white.json 载入白色样式
    data_white = obs.obs_data_create_from_json_file('white.json')

    # 将包含白色样式的数据对象合并至 data
    obs.obs_data_apply(data, data_white)
    # 输出 data 对应的 JSON 字符串
    json_string = obs.obs_data_get_json(data)
    obs.script_log(obs.LOG_INFO, json_string)

    # 从文件 black.json 载入黑色样式
    data_black = obs.obs_data_create_from_json_file('black.json')

    # 将包含黑色样式的数据对象合并至 data
    obs.obs_data_apply(data, data_black)
    # 输出 data 对应的 JSON 字符串
    json_string = obs.obs_data_get_json(data)
    obs.script_log(obs.LOG_INFO, json_string)

    # 获取场景中的文本源 Welcome
    source = obs.obs_get_source_by_name('Welcome')
    # 将样式应用到文本源
    obs.obs_source_update(source, data)

    # 释放数据对象和源对象
    obs.obs_data_release(data_black)
    obs.obs_data_release(data_white)
    obs.obs_data_release(data)
    obs.obs_source_release(source)
