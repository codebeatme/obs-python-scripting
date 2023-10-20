'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/data/create-data/ 如何创建数据
'''

# 导入模块 obspython
import obspython as obs

def script_properties():
    props = obs.obs_properties_create()

    # 添加一个选择背景图片的文件对话框
    prop = obs.obs_properties_add_path(props, 'path', '图片路径：', obs.OBS_PATH_FILE, '图片文件(*.jpg *.png)', None)
    obs.obs_property_set_modified_callback(prop, path_modified)

    return props

def path_modified(props, prop, settings):
    # 读取文件对话框确定的文件
    path = obs.obs_data_get_string(settings, 'path')

    # 如果用户还没有选择任何图片，则不设置图片源
    if path:
        # 获取场景中的图片源
        source = obs.obs_get_source_by_name('bg')

        # 将图片文件路径设置到图片源
        data = obs.obs_data_create()
        obs.obs_data_set_string(data, 'file', path)
        obs.obs_source_update(source, data)

        # 释放数据对象和源对象
        obs.obs_data_release(data)
        obs.obs_source_release(source)
