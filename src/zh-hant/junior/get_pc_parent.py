'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/script-properties/get-property-collection-parent/ 如何取得父級屬性集
'''

# 匯入模組 obspython
import obspython as obs

child_props = None

def script_properties():
    # 建立屬性集物件
    props = obs.obs_properties_create()

    # 添加一個文字方塊
    obs.obs_properties_add_text(props, 'first', '第一個文字方塊', obs.OBS_TEXT_DEFAULT)

    # 建立一個新的屬性集物件，作為 props 的子級
    global child_props
    child_props = obs.obs_properties_create()
    # 將一個按鈕添加至新的屬性集
    obs.obs_properties_add_button(child_props, 'find', '尋找文字方塊', find_clicked)

    # 添加一個群組方塊，他將包含新屬性集中的控製項
    obs.obs_properties_add_group(props, 'group', '群組方塊', obs.OBS_GROUP_NORMAL, child_props)

    return props


def find_clicked(props, prop):
    # 按鈕被點選時，將通過一些函式找到文字方塊，並取得他的說明資訊
    parent_props = obs.obs_properties_get_parent(child_props)
    first_prop = obs.obs_properties_first(parent_props)

    description = obs.obs_property_description(first_prop)
    obs.script_log(obs.LOG_INFO, f'說明為：{description}')
 