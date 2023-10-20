'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/script-properties/file-and-folder-dialog/ 如何使用文件对话框，文件夹对话框
'''

# 导入模块 obspython
import obspython as obs

def script_properties():
    props = obs.obs_properties_create()

    # 添加一个表示公告信息的多行文本框
    obs.obs_properties_add_text(props, 'announcement', '公告：', obs.OBS_TEXT_MULTILINE)
    # 添加一个选择公告文件的对话框
    obs.obs_properties_add_path(props, 'path', '公告路径：', obs.OBS_PATH_FILE, '文本文件(*.txt)', None)

    # 添加用于载入和保存公告的按钮
    obs.obs_properties_add_button(props, 'load', '载入', load_clicked)
    obs.obs_properties_add_button(props, 'save', '保存', save_clicked)

    return props

# 用于保存脚本设置
data = None

def script_load(settings):
    # 在脚本加载时，将脚本设置保存在模块变量 data 中
    global data
    data = settings

def load_clicked(props, prop):
    # 从文件载入公告信息并显示在多行文本框中
    path = obs.obs_data_get_string(data, 'path')

    # 如果用户还没有指定公告文件，则无法读取
    if path:
        # 从文件读取公告信息
        file = open(path, 'r', encoding='utf-8')
        content = file.read()
        file.close()

        # 将公告信息设置到文本框中
        obs.obs_data_set_string(data, 'announcement', content)
        obs.obs_properties_apply_settings(props, data)

    return True


def save_clicked(props, prop):
    # 将多行文本框中的内容保存到公告文件中
    path = obs.obs_data_get_string(data, 'path')

    # 如果用户还没有指定公告文件，则无法保存
    if path:
        # 获取多行文本框中的公告内容
        content = obs.obs_data_get_string(data, 'announcement')

        # 将公告内容写入文件
        file = open(path, 'w', encoding='utf-8')
        file.write(content)
        file.close()
