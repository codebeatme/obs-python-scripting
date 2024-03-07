# 导入模块 obspython
import obspython as obs


# 函数 load_message 将读取文本文件中的内容，并将其写入文本框
def load_message(props, prop, settings):
    # 获取文件对话框中的文件路径
    path = obs.obs_data_get_string(settings, 'more')

    if path:
        # 从文件读取内容
        file = open(path, 'r', encoding='utf-8')
        content = file.read()
        file.close()

        # 将内容设置到文本框中，如果内容与文本框不一致
        if content != obs.obs_data_get_string(settings, 'message'):
            obs.obs_data_set_string(settings, 'message', content)
            # 立即将脚本设置更新至控件，这将导致 load_message 再次被调用
            obs.obs_properties_apply_settings(props, settings)
            # 这里需要返回特定值 True
            return True

# 函数 set_source_color 将颜色对话框指定的颜色，设置到文本源
def set_source_color(settings):
    # 获取颜色对话框所确定的颜色
    color = obs.obs_data_get_int(settings, 'color')

    # 为场景中的文本源 Welcome 设置颜色
    source = obs.obs_get_source_by_name('Welcome')
    data = obs.obs_data_create()
    obs.obs_data_set_int(data, 'color', color)
    obs.obs_source_update(source, data)
    obs.obs_data_release(data)
    obs.obs_source_release(source)

# 函数 set_source_font 将字体对话框指定的字体，设置到文本源
def set_source_font(settings):
    # 获取字体对话框所确定的字体
    font = obs.obs_data_get_obj(settings, 'font')
    # obs.script_log(obs.LOG_INFO, f"颜色：{font}")
    
    # 为场景中的文本源 Welcome 设置字体
    source = obs.obs_get_source_by_name('Welcome')
    data = obs.obs_data_create()
    obs.obs_data_set_obj(data, 'font', font)
    obs.obs_source_update(source, data)
    obs.obs_data_release(font)
    obs.obs_data_release(data)
    obs.obs_source_release(source)

# 函数 set_source_text 将随机选择列表框中的项，然后将其设置为文本源的文本
def set_source_text(settings):
    # 获取列表框中的所有项
    my_texts = obs.obs_data_get_array(settings, 'my_texts')

    # 随机选择一个项，并将其内容设置为文本源的文本
    count = obs.obs_data_array_count(my_texts)
    if count > 0:
        import random
        index = random.randint(0, count - 1)
        item = obs.obs_data_array_item(my_texts, index)

        # 设置场景中的文本源 Welcome 的文本
        source = obs.obs_get_source_by_name('Welcome')
        data = obs.obs_data_create()
        obs.obs_data_set_string(data, 'text', obs.obs_data_get_string(item, 'value'))
        obs.obs_source_update(source, data)
        obs.obs_data_release(data)
        obs.obs_source_release(source)

# 用于登录的函数 login
def login(props, prop):
    # 点击登录按钮后，将隐藏分组框
    group_login = obs.obs_properties_get(props, 'group_login')
    obs.obs_property_set_visible(group_login, False)
    # 这里需要返回特定值 True，否则无法看到隐藏效果
    return True

# 让消息文本框显示随机的文本
def set_random_text(props, prop):
    # 随机的获取一个文本
    import random
    messages = ('天气不错！', '吃了吗？', '下雨啦！')
    text = messages[random.randint(0, 2)]

    # 将随机文本写入脚本设置项 message
    obs.obs_data_set_string(current_settings, 'message', text)
    # 将脚本设置应用到属性集对象
    obs.obs_properties_apply_settings(props, current_settings)
    # 这里需要返回特定值 True
    return True

def script_properties():
    # 创建一个属性集对象
    props = obs.obs_properties_create()

    # 添加一个复选框，用于控制是否在脚本载入后执行任务
    obs.obs_properties_add_bool(props, 'auto', '在启动时执行任务？')
    # 添加一个小数滑块，用于表示延迟执行任务的时间
    obs.obs_properties_add_float_slider(props, 'seconds', '延迟秒数', 1, 10, 0.5)
    # 添加一个文本框，用于表示需要发送的消息
    obs.obs_properties_add_text(props, 'message', '消息：', obs.OBS_TEXT_MULTILINE)
    # 添加一个按钮，用于再次执行 task 函数
    obs.obs_properties_add_button(props, 'again', '再次执行', lambda ps, p: task())

    # 添加一个组合框，用于选择直播平台
    platform = obs.obs_properties_add_list(props, 'platform', '直播平台：', obs.OBS_COMBO_TYPE_LIST, obs.OBS_COMBO_FORMAT_STRING)
    # 为组合框添加项，需要给出项的名称和值
    obs.obs_property_list_add_string(platform, 'YouTube', 'yt')
    obs.obs_property_list_add_string(platform, 'Twitch', 't')
    # 在组合框的第二个位置插入项，并使其不可用
    obs.obs_property_list_insert_string(platform, 1, 'Unkown', 'u')
    obs.obs_property_list_item_disable(platform, 1, True)

    # 添加一个文件对话框，用于加载更多的消息
    more = obs.obs_properties_add_path(props, 'more', '更多消息：', obs.OBS_PATH_FILE, '文本文件(*.txt)', None)
    # 当用户选择了一个文件后，函数 load_message 将被调用
    obs.obs_property_set_modified_callback(more, load_message)

    # 添加一个颜色对话框，用于设置文本源的颜色
    obs.obs_properties_add_color(props, 'color', '颜色：')
    # 添加一个字体对话框，用于设置文本源的字体
    obs.obs_properties_add_font(props, 'font', '字体：')

    # 添加一个可编辑列表框，用于设置文本源的文本
    obs.obs_properties_add_editable_list(props, 'my_texts', '文本源文本：', obs.OBS_EDITABLE_LIST_TYPE_STRINGS, None, None)

    # 创建分组框对应的属性集
    login_props = obs.obs_properties_create()
    # 添加一个分组框，他包含了用于登录的子控件
    obs.obs_properties_add_group(props, 'group_login', '用户登录', obs.OBS_GROUP_NORMAL, login_props)
    obs.obs_properties_add_text(login_props, 'username', '用户名称：', obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_text(login_props, 'password', '密码：', obs.OBS_TEXT_PASSWORD)
    # 添加一个登录按钮
    obs.obs_properties_add_button(login_props, 'login', '登录', login)

    # 添加一个按钮，用于为消息文本框选择随机文本
    obs.obs_properties_add_button(props, 'random_text', '随机消息', set_random_text)
    return props


def script_update(settings):
    # 用户编辑控件后，将最新的脚本设置应用至场景
    set_source_color(settings)
    set_source_font(settings)
    

def script_defaults(settings):
    # 设置控件的默认值
    obs.obs_data_set_default_bool(settings, 'auto', True)
    obs.obs_data_set_default_double(settings, 'seconds', 1.5)


# 变量 current_settings 用于表示脚本设置
current_settings = None

# 执行任务的函数 task
def task():
    obs.script_log(obs.LOG_INFO, '任务开始了')
    obs.remove_current_callback()

    # 显示文本框中的消息
    message = obs.obs_data_get_string(current_settings, 'message')
    obs.script_log(obs.LOG_INFO, f'消息为 {message if message else "[空]"}')
    # 显示选择的直播平台
    platform = obs.obs_data_get_string(current_settings, 'platform')
    obs.script_log(obs.LOG_INFO, f'直播平台为 {platform}')

    # 随机选择项作为文字源的文本
    set_source_text(current_settings)


def script_load(settings):
    global current_settings
    current_settings = settings

    # 是否在脚本载入后执行任务？
    if obs.obs_data_get_bool(settings, 'auto'):
        obs.script_log(obs.LOG_INFO, f'在启动时执行任务（是的）')

        # 添加运行任务的计时器，时间间隔为滑块表示的秒数
        seconds = obs.obs_data_get_double(settings, 'seconds')
        obs.script_log(obs.LOG_INFO, f'请等待大约 {seconds} 秒')
        obs.timer_add(task, int(seconds * 1000))
