# WARNING 该文件为测试文件，并不会产生预期效果
# 导入模块 obspython
import obspython as obs
import datetime

def script_properties():
    props = obs.obs_properties_create()

    # obs.obs_properties_set_flags(props, obs.obs_properties_get_flags(props) | obs.OBS_PROPERTIES_DEFER_UPDATE)

    # 添加一个表示消息的文本框
    obs.obs_properties_add_text(props, 'message', '消息：', obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_color(props, 'c', 'c')
    obs.obs_properties_add_int_slider(props, 'message1', '消息：', 1, 100, 3)


    return props

def script_update(settings):
    # 读取文本框对应的脚本设置项 message
    message = obs.obs_data_get_string(settings, 'message')
    obs.script_log(obs.LOG_INFO, f'消息更新为：{message}')
