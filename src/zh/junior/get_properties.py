'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/script-properties/get-properties/ 如何获取属性
'''

# 导入模块 obspython，datetime
import obspython as obs
import datetime

props = None


def script_properties():
    # 为脚本添加属性
    global props
    props = obs.obs_properties_create()

    # 计算当前是星期几
    day = datetime.datetime.now().weekday() + 1

    # 添加一个复选框，用来提醒自己是否需要直播，当然该功能并没有真的实现
    obs.obs_properties_add_bool(props, 'live', f'周 {day} 直播？')

    return props


def script_update(settings):
    # 当脚本更新时，显示复选框的相关状态
	# 使用 obs_properties_get 获取复选框相应的属性
    prop = obs.obs_properties_get(props, 'live')

    if prop:
        # 获取复选框的说明
        description = obs.obs_property_description(prop)

        # 获取脚本设置项 live，他表示复选框是否处于已选中状态
        live = obs.obs_data_get_bool(settings, 'live')
        obs.script_log(obs.LOG_INFO, f'{description}{live}')