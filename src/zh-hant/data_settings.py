# 匯入模組 obspython
import obspython as obs

# 根據 JSON 字串建立 OBS 資料設定物件
data = obs.obs_data_create_from_json('{"name":"Jack","age":12}')

# 取得不存在的項
obs.script_log(obs.LOG_INFO, f'取得不存在的項 nickname {obs.obs_data_get_string(data, "nickname") == ""}')
# 設定不存在的項
obs.obs_data_set_int(data, 'level', 100)
obs.script_log(obs.LOG_INFO, f'設定了不存在的項，level 為 {obs.obs_data_get_int(data, "level")}')

# 為項 balance 設定預設值，然後讀取
obs.obs_data_set_default_double(data, 'balance', 99.9)
obs.script_log(obs.LOG_INFO, f'balance 為 {obs.obs_data_get_double(data, "balance")}')

# 建立新的 OBS 資料設定物件並合併至 data
other_data = obs.obs_data_create_from_json('{"name":"Tom","enabled":true}')
obs.obs_data_apply(data, other_data)
obs.script_log(obs.LOG_INFO, f'name 為 {obs.obs_data_get_string(data, "name")}')
obs.script_log(obs.LOG_INFO, f'enabled 為 {obs.obs_data_get_bool(data, "enabled")}')

# 在刪除項 enabled 之前，為其指定預設值
obs.obs_data_set_default_bool(other_data, 'enabled', True)
obs.obs_data_erase(other_data, 'enabled')
# 項 enabled 被刪除之後，預設值也不再有效
obs.script_log(obs.LOG_INFO, f'other_data 中的 enabled 為 {obs.obs_data_get_bool(other_data, "enabled")}')

# 傳回資料設定物件的 JSON 字串
obs.script_log(obs.LOG_INFO, obs.obs_data_get_json(data))

# 儲存資料設定物件至檔案 player.json，如果檔案已經存在，則會將其備份為 player.json.backup
obs.obs_data_save_json_safe(data, 'player.json', '.temp', '.backup')

# 函式 add_hero 將一個英雄新增至 OBS 資料陣列物件
def add_hero(array, name, hp):
    # 建立表示英雄的資料設定物件 hero
    hero = obs.obs_data_create()
    obs.obs_data_set_string(hero, 'name', name)
    obs.obs_data_set_int(hero, 'hp', hp)

    # 將資料設定物件 hero 新增到資料陣列物件
    obs.obs_data_array_push_back(array, hero)
    obs.obs_data_release(hero)

# 建立一個 OBS 資料陣列物件 heroes
heroes = obs.obs_data_array_create()

# 呼叫 add_hero 新增一些英雄，他們具有隨機的生命值
import random
for i in range(10):
    add_hero(heroes, f'超人 {i}', random.randint(0, 100))

# 去掉所有生命值小於 50 的英雄
i = 0
while i < obs.obs_data_array_count(heroes):
    hero = obs.obs_data_array_item(heroes, i)

    if obs.obs_data_get_int(hero, 'hp') < 50:
        obs.obs_data_array_erase(heroes, i)
        obs.script_log(obs.LOG_INFO, f'英雄 {obs.obs_data_get_string(hero, "name")} 被刪除')
    else:
        i += 1

    obs.obs_data_release(hero)

# 顯示剩余英雄的個數
count = obs.obs_data_array_count(heroes)
obs.script_log(obs.LOG_INFO, f'剩余英雄 {count} 個')

# 將資料陣列物件 heroes 新增至資料設定物件
obs.obs_data_set_array(data, 'heroes', heroes)
obs.obs_data_array_release(heroes)

# 釋放對資料設定物件的參考
obs.obs_data_release(data)
obs.obs_data_release(other_data)