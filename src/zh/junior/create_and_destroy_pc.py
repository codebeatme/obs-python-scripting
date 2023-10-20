'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/script-properties/create-and-destroy-property-collections/ 如何创建和销毁属性集
'''

# 导入模块 obspython，datetime
import obspython as obs
import datetime

# 开始时间
start = None

def script_properties():
    # script_properties 返回一个属性集对象
    # 调用 obs_properties_create 函数创建属性集
    props = obs.obs_properties_create()

    # 添加一个判断是否可以结束直播的按钮
    obs.obs_properties_add_button(props, 'over', '结束了？', over_clicked)

    # 将当前时间记录为开始时间
    global start
    start = datetime.datetime.now()

    return props

def over_clicked(props, prop):
    # 当按钮被点击时，判断是否可以结束直播

    # 计算从开始时间到现在经历的秒数
    end = datetime.datetime.now()
    seconds = (end - start).total_seconds()

    # 已经过了 1 分钟，则显示可以结束
    if seconds > 60:
        obs.script_log(obs.LOG_INFO, '可以结束了')
    else:
        obs.script_log(obs.LOG_INFO, '直播还不到 1 分钟')
