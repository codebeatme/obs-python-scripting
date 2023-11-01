'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/data/data-array/ 如何使用数据数组
'''

# 导入模块 obspython
import obspython as obs

# 用于保存脚本设置
data = None

def script_load(settings):
    # 在脚本加载时，将脚本设置保存在模块变量 data 中
    global data
    data = settings

    heros = obs.obs_data_get_array(settings, 'heros')

    # 如果设置项 heros 不存在，则添加
    if not heros:
        # 创建一个数据数组对象
        heros = obs.obs_data_array_create()

        # 为数组添加表示英雄的数据对象
        add_hero(heros, '咸蛋超人', 100)
        add_hero(heros, '鸭蛋超人', 200)

        # 将数组对象添加为设置项 heros
        obs.obs_data_set_array(settings, 'heros', heros)

    obs.obs_data_array_release(heros)

def add_hero(array, name, hp):
    # 创建表示英雄的数据对象
    hero = obs.obs_data_create()
    obs.obs_data_set_string(hero, 'name', name)
    obs.obs_data_set_int(hero, 'hp', hp)

    # 将数据对象添加到数组
    obs.obs_data_array_push_back(array, hero)
    obs.obs_data_release(hero)

    # 获取数组的大小
    count = obs.obs_data_array_count(array)
    obs.script_log(obs.LOG_INFO, f'已添加英雄 {name}，现有英雄 {count} 个')

def script_properties():
    props = obs.obs_properties_create()

    # 添加一个按钮，用于清除数组中的第一个英雄
    obs.obs_properties_add_button(props, 'remove', '移除一个英雄', remove_clicked)

    return props

def remove_clicked(props, prop):
    heros = obs.obs_data_get_array(data, 'heros')

    # 如果数组中还有英雄，则删除其中的第一个
    if obs.obs_data_array_count(heros):
        # 在删除第一个英雄之前，获取并显示该英雄的相关信息
        hero = obs.obs_data_array_item(heros, 0)
        obs.obs_data_array_erase(heros, 0)

        name = obs.obs_data_get_string(hero, 'name')
        hp = obs.obs_data_get_int(hero, 'hp')
        obs.obs_data_release(hero)

        obs.script_log(obs.LOG_INFO, f'已删除英雄 {name} {hp}')
    else:
        obs.script_log(obs.LOG_INFO, '英雄全挂了哦！')

    obs.obs_data_array_release(heros)