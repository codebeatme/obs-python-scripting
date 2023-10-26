'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/data/get-and-set-data-item-default-value/ 如何获取和设置数据项的默认值
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

    # 添加设置消息内容的文本框
    obs.obs_properties_add_text(props, 'message', '消息：', obs.OBS_TEXT_DEFAULT)

    # 添加选择延迟时间的组合框
    prop = obs.obs_properties_add_list(props, 'time', '延迟时间：', obs.OBS_COMBO_TYPE_LIST, obs.OBS_COMBO_FORMAT_STRING)
    obs.obs_property_list_add_string(prop, '长', 'long')
    obs.obs_property_list_add_string(prop, '短', 'short')

    # 添加一个显示消息的按钮
    obs.obs_properties_add_button(props, 'show', '显示', show_clicked)

    return props


def script_defaults(settings):
    # 为脚本设置项设置默认值，包括默认消息和延迟时间
    obs.obs_data_set_default_string(settings, 'message', '这是默认消息')
    obs.obs_data_set_default_string(settings, 'time', 'short')


def show_clicked(props, prop):
    # 根据用户选择的延迟时间，决定延迟的秒数
    time = obs.obs_data_get_string(data, 'time')
    seconds = None

    if time == 'long':
        seconds = 3
    elif time == 'short':
        seconds = 1

    if seconds:
        # 添加计时器，时间间隔为指定的秒数
        obs.timer_add(log, 1000 * seconds)
        obs.script_log(obs.LOG_INFO, f'{seconds} 秒后显示消息')


def log():
    message = obs.obs_data_get_string(data, 'message')
    obs.script_log(obs.LOG_INFO, message)

    # 移除之前添加的计时器
    obs.remove_current_callback()

