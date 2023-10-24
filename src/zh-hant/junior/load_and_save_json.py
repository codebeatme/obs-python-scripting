'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/data/load-and-save-json/ 如何載入和儲存 JSON
'''

# 匯入模組 obspython
import obspython as obs

def script_properties():
    props = obs.obs_properties_create()

    # 添加儲存和載入 JSON 檔案的按鈕
    obs.obs_properties_add_button(props, 'save', '儲存', save_clicked)
    obs.obs_properties_add_button(props, 'load', '載入', load_clicked)

    return props

# 玩家經驗值
exp = 0
# 玩家等級
level = 0

def save_clicked(props, prop):
    # 建立資料物件，並寫入玩家資訊
    data = obs.obs_data_create()
    obs.obs_data_set_int(data, 'exp', exp)
    obs.obs_data_set_int(data, 'level', level)

    # 將資料物件儲存至檔案 player.json，如果檔案存在，則先將其備份為 player.backup.json
    obs.obs_data_save_json_safe(data, 'player.json', '.temp', '.backup')
    # 釋放資料物件
    obs.obs_data_release(data)

def load_clicked(props, prop):
    global exp, level

    # 從檔案 player.json 載入玩家資訊
    data = obs.obs_data_create_from_json_file_safe('player.json', '.backup')

    # 讀取玩家的經驗值和等級
    exp = obs.obs_data_get_int(data, 'exp')
    level = obs.obs_data_get_int(data, 'level')
    # 釋放資料物件
    obs.obs_data_release(data)
    
    obs.script_log(obs.LOG_INFO, f'經驗值：{exp}，等級：{level}')
