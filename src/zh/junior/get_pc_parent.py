'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/script-properties/get-property-collection-parent/ 如何获取父级属性集
'''

# 导入模块 obspython
import obspython as obs

child_props = None

def script_properties():
    # 创建属性集对象
    props = obs.obs_properties_create()

    # 添加一个文本框
    obs.obs_properties_add_text(props, 'first', '第一个文本框', obs.OBS_TEXT_DEFAULT)

    # 创建一个新的属性集对象，作为 props 的子级
    global child_props
    child_props = obs.obs_properties_create()
    # 将一个按钮添加至新的属性集
    obs.obs_properties_add_button(child_props, 'find', '查找文本框', find_clicked)

    # 添加一个分组框，他将包含新属性集中的控件
    obs.obs_properties_add_group(props, 'group', '分组框', obs.OBS_GROUP_NORMAL, child_props)

    return props


def find_clicked(props, prop):
    # 按钮被点击时，将通过一些函数找到文本框，并获取他的说明信息
    parent_props = obs.obs_properties_get_parent(child_props)
    first_prop = obs.obs_properties_first(parent_props)

    description = obs.obs_property_description(first_prop)
    obs.script_log(obs.LOG_INFO, f'说明为：{description}')
 