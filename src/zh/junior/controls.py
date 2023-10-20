'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/script-properties/general-control-functions/ 通用控件函数有哪些
'''

# 导入模块 obspython
import obspython as obs

def script_properties():
    props = obs.obs_properties_create()

    # 添加一个按钮，用于确定一些直播的设置
    obs.obs_properties_add_button(props, 'ok', '确定', ok_clicked)

    # 添加一个复选框，表示直播是否显示欢迎消息
    prop = obs.obs_properties_add_bool(props, 'display_welcome', '是否显示欢迎消息？')
    obs.obs_property_set_modified_callback(prop, display_welcome_modified)

    # 添加一个文本框，表示欢迎消息
    prop = obs.obs_properties_add_text(props, 'welcome', '欢迎消息：', obs.OBS_TEXT_DEFAULT)
    # 设置文本框不显示
    obs.obs_property_set_visible(prop, False)

    return props

def ok_clicked(props, prop):
    # 确定按钮不能被再一次的点击
    obs.obs_property_set_enabled(prop, False)

    # 如果文本框可见，则认为显示欢迎消息
    prop_welcome = obs.obs_properties_get(props, 'welcome')
    obs.script_log(obs.LOG_INFO, f'显示欢迎消息？{obs.obs_property_visible(prop_welcome)}')
    return True

def display_welcome_modified(props, prop, settings):
    # 点击复选框时，切换文本框的可见状态
    # 获取文本框
    prop_welcome = obs.obs_properties_get(props, 'welcome')

    # 获取并反转文本框的可见状态
    visible = not obs.obs_property_visible(prop_welcome)
    obs.obs_property_set_visible(prop_welcome, visible)
    return True
