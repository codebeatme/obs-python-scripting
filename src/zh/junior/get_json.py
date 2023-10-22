'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/data/get-json-from-data/ 如何从数据获取 JSON
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

    # 添加设置项 message
    obs.obs_data_set_string(data, 'message', '你好！')

    # 添加两个按钮
    obs.obs_properties_add_button(props, 'json', '获取设置的 JSON', json_clicked)
    obs.obs_properties_add_button(props, 'last_json', '最后的 JSON', last_json_clicked)

    return props

def json_clicked(props, prop):
    # 获取脚本设置对应的 JSON 字符串
    json = obs.obs_data_get_json(data)
    obs.script_log(obs.LOG_INFO, f'设置的 JSON：{json}')

    # 修改设置项 message
    obs.obs_data_set_string(data, 'message', '再见！')


def last_json_clicked(props, prop):
    # 获取上一次脚本设置生成的 JSON 字符串
    json = obs.obs_data_get_last_json(data)
    obs.script_log(obs.LOG_INFO, f'最后的 JSON：{json}')
