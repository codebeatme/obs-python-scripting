# WARNING 该文件为测试文件，并不会产生预期效果
# 导入模块 obspython
import obspython as obs

prop_message = None

def script_properties():
    props = obs.obs_properties_create()

    global prop_message
    # 添加一个文本框，表示欢迎消息
    prop_message = obs.obs_properties_add_text(props, 'welcome', '欢迎消息：', obs.OBS_TEXT_DEFAULT)

    return props

def script_update(settings):
    # 函数 script_update 会在脚本更新时被调用
    # 读取脚本设置项 hours 并显示
    
    if obs.obs_property_modified(prop_message, settings):
        obs.script_log(obs.LOG_INFO, '欢迎消息已经被修改')