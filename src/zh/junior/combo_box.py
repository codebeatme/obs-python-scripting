'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/script-properties/combo-box/ 如何使用组合框
'''

# 导入模块 obspython
import obspython as obs

def script_properties():
    props = obs.obs_properties_create()

    # 添加一个表示直播平台的组合框
    prop = obs.obs_properties_add_list(props, 'platform', '直播平台：', obs.OBS_COMBO_TYPE_LIST, obs.OBS_COMBO_FORMAT_STRING)

    # 为组合框添加项
    obs.obs_property_list_add_string(prop, 'YouTube', 'yt')
    obs.obs_property_list_add_string(prop, 'Twitch', 't')
    # 在组合框的第二个位置插入项，并使该项不可用
    obs.obs_property_list_insert_string(prop, 1, 'Unkown', 'u')
    obs.obs_property_list_item_disable(prop, 1, True)

    # 增加一个开始直播的按钮
    obs.obs_properties_add_button(props, 'start', '开始直播', start_clicked)

    return props

# 用于保存脚本设置
data = None

def script_load(settings):
    # 在脚本加载时，将脚本设置保存在模块变量 data 中
    global data
    data = settings

def start_clicked(props, prop):
    # 获取组合框中选中的项，并显示在脚本日志窗口中
    platform = obs.obs_data_get_string(data, 'platform')

    obs.script_log(obs.LOG_INFO, f'开始在 {platform} 直播')