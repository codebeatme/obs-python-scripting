'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/script-properties/apply-settings-to-property-collection/ 如何应用设置至属性集
'''

# 导入模块 obspython，random
import obspython as obs
import random

# 用于保存脚本设置
data = None
# 一组可供选择的消息
messages = ('天气不错！', '吃了吗？', '下雨啦！')


def script_load(settings):
    # 在脚本加载时，将脚本设置保存在模块变量 data 中
    global data
    data = settings


def script_properties():
    props = obs.obs_properties_create()

    # 添加一个文本框和按钮
    obs.obs_properties_add_text(props, 'message', '消息：', obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_button(props, 'random_message', '随机消息', random_message_clicked)

    return props


def random_message_clicked(props, prop):
    # 随机的获取一个消息
    message = messages[random.randint(0, 2)]

    # 将消息写入脚本设置项 message
    obs.obs_data_set_string(data, 'message', message)
    # 将脚本设置应用到脚本属性集
    obs.obs_properties_apply_settings(props, data)
    return True
