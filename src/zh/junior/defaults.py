'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/script-function-exports/set-script-setting-default-values/ 如何设置脚本设置的默认值
'''

# 导入模块 obspython
import obspython as obs

def script_properties():
    # 添加一个控制是否自动运行的复选框
    props = obs.obs_properties_create()
    obs.obs_properties_add_bool(props, 'autorun', '自动运行')

    return props

def script_defaults(settings):
    # 函数 script_defaults 用于设置脚本设置的默认值
    # 将设置项 autorun 的默认值设置为 True
    obs.obs_data_set_default_bool(settings, 'autorun', True)

def script_load(settings):
    # 在脚本加载时，读取设置项 autorun
    autorun = obs.obs_data_get_bool(settings, 'autorun')

    # 如果是自动运行，则输出一段文字信息
    if autorun:
        obs.script_log(obs.LOG_INFO, '自动运行已经开启')
