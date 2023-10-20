'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/data/add-and-release-data-reference/ 如何添加和释放数据引用
'''

# 导入模块 obspython
import obspython as obs

# 一个数据对象
data = None


def script_properties():
    global data
    props = obs.obs_properties_create()

    # 创建一个数据对象，包含了姓名和年龄
    data = obs.obs_data_create()
    obs.obs_data_set_string(data, 'name', '保密的哦！')
    obs.obs_data_set_int(data, 'age', 77)

    # 为数据对象添加新的引用，将需要调用两次 obs_data_release
    obs.obs_data_addref(data)

    # 添加显示姓名和年龄的按钮
    obs.obs_properties_add_button(props, 'show_name', '显示姓名', show_name_clicked)
    obs.obs_properties_add_button(props, 'show_age', '显示年龄', show_age_clicked)

    return props


def show_name_clicked(props, prop):
    # 显示姓名，然后释放对数据对象的一个引用
    name = obs.obs_data_get_string(data, 'name')
    obs.script_log(obs.LOG_INFO, f'姓名：{name}')
    # 释放数据对象
    obs.obs_data_release(data)


def show_age_clicked(props, prop):
    # 显示年龄，然后释放对数据对象的一个引用
    age = obs.obs_data_get_int(data, 'age')
    obs.script_log(obs.LOG_INFO, f'年龄：{age}')
    # 释放数据对象
    obs.obs_data_release(data)
