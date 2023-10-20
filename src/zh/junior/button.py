'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/script-properties/button/ 如何使用按钮
'''

# 导入模块 obspython
import obspython as obs

def script_properties():
    props = obs.obs_properties_create()

    # 添加一个按钮
    prop = obs.obs_properties_add_button(props, 'output', '输出', output_clicked)
    # 设置按钮的类型和 URL，回调函数 output_clicked 将失效
    obs.obs_property_button_set_type(prop, obs.OBS_BUTTON_URL)
    obs.obs_property_button_set_url(prop, 'http://www.bing.com/')

    return props

def output_clicked(props, prop):
    # 获取按钮的 URL，并输出到脚本日志窗口中，但这不会发生
    url = obs.obs_property_button_url(prop)
    obs.script_log(obs.LOG_INFO, f'按钮 URL：{url}')