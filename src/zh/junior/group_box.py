'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/script-properties/group-box/ 如何使用分组框
'''

# 导入模块 obspython
import obspython as obs

def script_properties():
    props = obs.obs_properties_create()

    # 创建登录分组框对应的属性集
    login_props = obs.obs_properties_create()
    # 添加登录分组框
    obs.obs_properties_add_group(props, 'group_login', '用户登录', obs.OBS_GROUP_NORMAL, login_props)

    # 为登录分组框添加文本框和按钮
    obs.obs_properties_add_text(login_props, 'user_name', '用户名称：', obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_text(login_props, 'password', '密码：', obs.OBS_TEXT_PASSWORD)
    obs.obs_properties_add_button(login_props, 'login', '登录', login_clicked)

    # 添加一个用来在成功登录后显示的文本框，登录前并不显示
    prop_welcome = obs.obs_properties_add_text(props, 'welcome', '欢迎：', obs.OBS_TEXT_INFO)
    obs.obs_property_set_visible(prop_welcome, False)

    return props


# 用于保存脚本设置
data = None


def script_load(settings):
    # 在脚本加载时，将脚本设置保存在模块变量 data 中
    global data
    data = settings

def login_clicked(props, prop):
    # 获取用户输入的用户名称和密码
    user_name = obs.obs_data_get_string(data, 'user_name')
    password = obs.obs_data_get_string(data, 'password')

    # 简单的判断登录信息，登录成功则执行一些操作
    if user_name == 'hero' and password == '123':
        # 隐藏登录分组框
        prop_group = obs.obs_properties_get(props, 'group_login')
        obs.obs_property_set_visible(prop_group, False)

        # 使 welcome 文本框可见，并展示用户名称
        prop_welcome = obs.obs_properties_get(props, 'welcome')
        obs.obs_data_set_string(data, 'welcome', f'用户 {user_name}')
        obs.obs_properties_apply_settings(props, data)
        obs.obs_property_set_visible(prop_welcome, True)

    return True