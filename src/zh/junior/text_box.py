'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/script-properties/text-box/ 如何使用文本框
'''

# 导入模块 obspython
import obspython as obs


def script_properties():
    props = obs.obs_properties_create()

    # 添加一个表示用户名称的文本框
    obs.obs_properties_add_text(props, 'user_name', '用户名称：', obs.OBS_TEXT_DEFAULT)
    # 添加一个表示密码的文本框
    obs.obs_properties_add_text(props, 'password', '密码：', obs.OBS_TEXT_PASSWORD)

    # 添加一个只读的文本框，用于显示登录的结果
    obs.obs_properties_add_text(props, 'info', '结果：', obs.OBS_TEXT_INFO)
    # 清除上一次显示的登录结果
    set_info(props, '', obs.OBS_TEXT_INFO_NORMAL)

    # 添加一个用于登录的按钮
    obs.obs_properties_add_button(props, 'login', '登录', login_clicked)

    return props


# 用于保存脚本设置
data = None


def script_load(settings):
    # 在脚本加载时，将脚本设置保存在模块变量 data 中
    global data
    data = settings


def set_info(props, content, type):
    # 设置只读文本框所显示的内容
    obs.obs_data_set_string(data, 'info', content)
    obs.obs_properties_apply_settings(props, data)

    # 设置只读文本框的信息类型
    prop = obs.obs_properties_get(props, 'info')
    obs.obs_property_text_set_info_type(prop, type)


def login_clicked(props, prop):
    # 登录按钮被点击时，获取并验证用户名称和密码
    user_name = obs.obs_data_get_string(data, 'user_name')
    password = obs.obs_data_get_string(data, 'password')

    # 简单的判断用户名称和密码，并显示不同的消息
    if user_name == 'abc' and password == 'abc':
        set_info(props, '登录成功！', obs.OBS_TEXT_INFO_NORMAL)
    else:
        set_info(props, '用户名称或密码错误！', obs.OBS_TEXT_INFO_WARNING)

    return True
