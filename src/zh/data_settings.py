# 导入模块 obspython
import obspython as obs

# 根据 JSON 字符串创建 OBS 数据设置对象
data = obs.obs_data_create_from_json('{"name":"Jack","age":12}')

# 获取不存在的项
obs.script_log(obs.LOG_INFO, f'获取不存在的项 nickname {obs.obs_data_get_string(data, "nickname") == ""}')
# 设置不存在的项
obs.obs_data_set_int(data, 'level', 100)
obs.script_log(obs.LOG_INFO, f'设置了不存在的项，level 为 {obs.obs_data_get_int(data, "level")}')

# 为项 balance 设置默认值，然后读取
obs.obs_data_set_default_double(data, 'balance', 99.9)
obs.script_log(obs.LOG_INFO, f'balance 为 {obs.obs_data_get_double(data, "balance")}')

# 创建新的 OBS 数据设置对象并合并至 data
other_data = obs.obs_data_create_from_json('{"name":"Tom","enabled":true}')
obs.obs_data_apply(data, other_data)
obs.script_log(obs.LOG_INFO, f'name 为 {obs.obs_data_get_string(data, "name")}')
obs.script_log(obs.LOG_INFO, f'enabled 为 {obs.obs_data_get_bool(data, "enabled")}')

# 在删除项 enabled 之前，为其指定默认值
obs.obs_data_set_default_bool(other_data, 'enabled', True)
obs.obs_data_erase(other_data, 'enabled')
# 项 enabled 被删除之后，默认值也不再有效
obs.script_log(obs.LOG_INFO, f'other_data 中的 enabled 为 {obs.obs_data_get_bool(other_data, "enabled")}')

# 返回数据设置对象的 JSON 字符串
obs.script_log(obs.LOG_INFO, obs.obs_data_get_json(data))

# 保存数据设置对象至文件 player.json，如果文件已经存在，则会将其备份为 player.json.backup
obs.obs_data_save_json_safe(data, 'player.json', '.temp', '.backup')

# 函数 add_hero 将一个英雄添加至 OBS 数据数组对象
def add_hero(array, name, hp):
    # 创建表示英雄的数据设置对象 hero
    hero = obs.obs_data_create()
    obs.obs_data_set_string(hero, 'name', name)
    obs.obs_data_set_int(hero, 'hp', hp)

    # 将数据设置对象 hero 添加到数据数组对象
    obs.obs_data_array_push_back(array, hero)
    obs.obs_data_release(hero)

# 创建一个 OBS 数据数组对象 heroes
heroes = obs.obs_data_array_create()

# 调用 add_hero 添加一些英雄，他们具有随机的生命值
import random
for i in range(10):
    add_hero(heroes, f'超人 {i}', random.randint(0, 100))

# 去掉所有生命值小于 50 的英雄
i = 0
while i < obs.obs_data_array_count(heroes):
    hero = obs.obs_data_array_item(heroes, i)

    if obs.obs_data_get_int(hero, 'hp') < 50:
        obs.obs_data_array_erase(heroes, i)
        obs.script_log(obs.LOG_INFO, f'英雄 {obs.obs_data_get_string(hero, "name")} 被删除')
    else:
        i += 1

    obs.obs_data_release(hero)

# 显示剩余英雄的个数
count = obs.obs_data_array_count(heroes)
obs.script_log(obs.LOG_INFO, f'剩余英雄 {count} 个')

# 将数据数组对象 heroes 添加至数据设置对象
obs.obs_data_set_array(data, 'heroes', heroes)
obs.obs_data_array_release(heroes)

# 释放对数据设置对象的引用
obs.obs_data_release(data)
obs.obs_data_release(other_data)