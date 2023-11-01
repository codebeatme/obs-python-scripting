'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/data/data-array/ 如何使用資料陣列
'''

# 匯入模組 obspython
import obspython as obs

# 用於儲存腳本設定
data = None

def script_load(settings):
    # 在腳本載入時，將腳本設定儲存在模組變數 data 中
    global data
    data = settings

    heros = obs.obs_data_get_array(settings, 'heros')

    # 如果設定項 heros 不存在，則添加
    if not heros:
        # 建立一個資料陣列物件
        heros = obs.obs_data_array_create()

        # 為陣列添加表示英雄的資料物件
        add_hero(heros, '鹹蛋超人', 100)
        add_hero(heros, '鴨蛋超人', 200)

        # 將陣列物件添加為設定項 heros
        obs.obs_data_set_array(settings, 'heros', heros)

    obs.obs_data_array_release(heros)

def add_hero(array, name, hp):
    # 建立表示英雄的資料物件
    hero = obs.obs_data_create()
    obs.obs_data_set_string(hero, 'name', name)
    obs.obs_data_set_int(hero, 'hp', hp)

    # 將資料物件添加到陣列
    obs.obs_data_array_push_back(array, hero)
    obs.obs_data_release(hero)

    # 取得陣列的大小
    count = obs.obs_data_array_count(array)
    obs.script_log(obs.LOG_INFO, f'已添加英雄 {name}，現有英雄 {count} 個')

def script_properties():
    props = obs.obs_properties_create()

    # 添加一個按鈕，用於清除陣列中的第一個英雄
    obs.obs_properties_add_button(props, 'remove', '移除一個英雄', remove_clicked)

    return props

def remove_clicked(props, prop):
    heros = obs.obs_data_get_array(data, 'heros')

    # 如果陣列中還有英雄，則刪除其中的第一個
    if obs.obs_data_array_count(heros):
        # 在刪除第一個英雄之前，取得並顯示該英雄的相關資訊
        hero = obs.obs_data_array_item(heros, 0)
        obs.obs_data_array_erase(heros, 0)

        name = obs.obs_data_get_string(hero, 'name')
        hp = obs.obs_data_get_int(hero, 'hp')
        obs.obs_data_release(hero)

        obs.script_log(obs.LOG_INFO, f'已刪除英雄 {name} {hp}')
    else:
        obs.script_log(obs.LOG_INFO, '英雄全掛了哦！')

    obs.obs_data_array_release(heros)