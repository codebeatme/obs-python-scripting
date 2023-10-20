'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/script-function-exports/add-script-properties/ 如何添加脚本属性
'''

# 导入模块 obspython
import obspython as obs


def script_properties():
    # 函数 script_properties 用于提供脚本属性
    # 创建一个表示属性集的对象
    props = obs.obs_properties_create()

    # 添加文本框，其对应的脚本设置项名称为 message
    obs.obs_properties_add_text(props, 'message', '消息：', obs.OBS_TEXT_DEFAULT)
    # 添加按钮，其对应的脚本设置项名称为 output，点击按钮将调用函数 output_clicked
    obs.obs_properties_add_button(props, 'output', '输出到日志', output_clicked)

    return props


def output_clicked(props, prop):
    # 当按钮被点击时，获取 message 设置项，并在脚本日志中显示
    message = obs.obs_data_get_string(data, 'message')
    obs.script_log(obs.LOG_INFO, message)


# 在模块中定义变量 data，用来表示脚本的设置
data = None

def script_load(settings):
    global data
    # 在脚本载入时，将脚本设置赋值给 data
    data = settings
