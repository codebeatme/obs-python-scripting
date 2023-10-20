'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/data/clear-data-items-and-erase-data-item/ 如何清除所有数据项，擦除数据项
'''

# 导入模块 obspython
import obspython as obs

# 用于保存脚本设置
data = None

def script_load(settings):
    # 在脚本加载时，将脚本设置保存在模块变量 data 中
    global data
    data = settings

def script_properties():
    props = obs.obs_properties_create()

    # 添加用于填写玩家和游戏信息的文本框
    obs.obs_properties_add_text(props, 'player', '玩家：', obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_text(props, 'game', '游戏：', obs.OBS_TEXT_DEFAULT)
    # 添加显示祝贺信息的文本框
    obs.obs_properties_add_text(props, 'done', '祝贺，你已经完成所有步骤！', obs.OBS_TEXT_INFO)
    # 添加下一步和重置按钮
    obs.obs_properties_add_button(props, 'next', '下一步', next_clicked)
    obs.obs_properties_add_button(props, 'reset', '重置', reset_clicked)

    # 刷新界面，用于显示或隐藏文本框和按钮
    refresh_ui(props)

    return props

def next_clicked(props, prop):
    # 当下一步按钮被点击时，将脚本设置项 step 加 1，表示进入下一步
    step = obs.obs_data_get_int(data, 'step')
    obs.obs_data_set_int(data, 'step', step + 1)

    # 刷新界面，切换显示下一步所用的控件
    refresh_ui(props)
    return True

def reset_clicked(props, prop):
    # 清空所有的脚本设置项
    obs.obs_data_clear(data)
    # 需要将脚本设置应用到属性，否则文本框中的已有内容不会被清空
    obs.obs_properties_apply_settings(props, data)

    # 刷新界面，恢复到第一步
    refresh_ui(props)
    return True

def refresh_ui(props):
    # 脚本设置项 step 表示当前是第几步
    step = obs.obs_data_get_int(data, 'step')

    # 根据 step 来决定哪些文本框和按钮需要显示
    prop = obs.obs_properties_get(props, 'player')
    obs.obs_property_set_visible(prop, step == 0)

    prop = obs.obs_properties_get(props, 'game')
    obs.obs_property_set_visible(prop, step == 1)

    prop = obs.obs_properties_get(props, 'done')
    obs.obs_property_set_visible(prop, step == 2)

    prop = obs.obs_properties_get(props, 'next')
    obs.obs_property_set_visible(prop, step != 2)

    prop = obs.obs_properties_get(props, 'reset')
    obs.obs_property_set_visible(prop, step == 2)