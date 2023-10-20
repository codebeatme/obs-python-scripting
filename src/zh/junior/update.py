'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/script-function-exports/script-updating-and-saving/ 脚本更新，脚本保存
'''

# 导入模块 obspython
import obspython as obs


def script_properties():
    # 添加一个表示小时的数字显示框
    props = obs.obs_properties_create()
    obs.obs_properties_add_int(props, 'hours', '小时：', 2, 5, 1)

    return props


def script_update(settings):
    # 函数 script_update 会在脚本更新时被调用
    # 读取脚本设置项 hours 并显示
    hours = obs.obs_data_get_int(settings, 'hours')
    obs.script_log(obs.LOG_INFO, f'小时更新为：{hours}')
