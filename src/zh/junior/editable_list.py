'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/script-properties/editable-list/ 如何使用可编辑列表框
'''

# 导入模块 obspython，random
import obspython as obs
import random


def script_properties():
    props = obs.obs_properties_create()

    # 添加一个表示颜色的可编辑列表框
    obs.obs_properties_add_editable_list(props, 'colors', '颜色：', obs.OBS_EDITABLE_LIST_TYPE_STRINGS, None, None)

    # 增加一个随机选择颜色的按钮
    obs.obs_properties_add_button(props, 'select_color', '选择颜色', select_color_clicked)

    return props


# 用于保存脚本设置
data = None


def script_load(settings):
    # 在脚本加载时，将脚本设置保存在模块变量 data 中
    global data
    data = settings


def select_color_clicked(props, prop):
    # 随机的选择一个颜色，并显示在脚本日志窗口中

    # 获取所有的颜色
    items = obs.obs_data_get_array(data, 'colors')
    # 获取颜色的数量
    count = obs.obs_data_array_count(items)

    # 随机的选择一个颜色，并获取颜色的值
    index = random.randint(0, count - 1)
    item = obs.obs_data_array_item(items, index)
    color = obs.obs_data_get_string(item, 'value')

    obs.script_log(obs.LOG_INFO, f'选择了颜色：{color}')
