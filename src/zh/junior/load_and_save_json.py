'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/data/load-and-save-json/ 如何加载和保存 JSON
'''

# 导入模块 obspython
import obspython as obs

def script_properties():
    props = obs.obs_properties_create()

    # 添加保存和载入 JSON 文件的按钮
    obs.obs_properties_add_button(props, 'save', '保存', save_clicked)
    obs.obs_properties_add_button(props, 'load', '载入', load_clicked)

    return props

# 玩家经验值
exp = 0
# 玩家等级
level = 0

def save_clicked(props, prop):
    # 创建数据对象，并写入玩家信息
    data = obs.obs_data_create()
    obs.obs_data_set_int(data, 'exp', exp)
    obs.obs_data_set_int(data, 'level', level)

    # 将数据对象保存至文件 player.json，如果文件存在，则先将其备份为 player.backup.json
    obs.obs_data_save_json_safe(data, 'player.json', '.temp', '.backup')
    # 释放数据对象
    obs.obs_data_release(data)

def load_clicked(props, prop):
    global exp, level

    # 从文件 player.json 载入玩家信息
    data = obs.obs_data_create_from_json_file_safe('player.json', '.backup')

    # 读取玩家的经验值和等级
    exp = obs.obs_data_get_int(data, 'exp')
    level = obs.obs_data_get_int(data, 'level')
    # 释放数据对象
    obs.obs_data_release(data)
    
    obs.script_log(obs.LOG_INFO, f'经验值：{exp}，等级：{level}')
