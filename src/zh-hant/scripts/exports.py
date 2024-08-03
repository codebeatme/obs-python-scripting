# 匯入模組 obspython
import obspython as obs

def script_description():
    return '這是一個簡單但沒有任何效果的腳本\n作者：\t哎呦餵\n版本：\t0.1\n聯系：\txxx'

def script_properties():
    # 建立一個屬性集物件
    props = obs.obs_properties_create()

    # 新增一個對應微調方塊的腳本屬性物件，用於表示小時
    obs.obs_properties_add_int(props, 'hours', '小時：', 2, 5, 1)
    return props

# 變數 data 表示腳本設定
data = None

def script_load(settings):
    global data
    data = settings

    # 讀取腳本設定項 closed_time，他是腳本的停止時間
    closed_time = obs.obs_data_get_string(data, 'closed_time')
    if closed_time:
        obs.script_log(obs.LOG_INFO, f'上次腳本停止的時間為 {closed_time}')

    obs.script_log(obs.LOG_INFO, script_path())

# def script_unload():
#     # 將目前時間寫入腳本設定項 closed_time，作為腳本的停止時間
#     from datetime import datetime
#     obs.obs_data_set_string(data, 'closed_time', datetime.now().ctime())

def script_update(settings):
    # 讀取腳本設定項 hours 並顯示
    hours = obs.obs_data_get_int(settings, 'hours')
    obs.script_log(obs.LOG_INFO, f'目前小時為 {hours}')

def script_save(settings):
	# 將目前時間寫入腳本設定項 closed_time，作為腳本的停止時間
	from datetime import datetime
	obs.obs_data_set_string(settings, 'closed_time', datetime.now().ctime())

def script_defaults(settings):
	# 將設定項 hours 的預設值設定為 3
	obs.obs_data_set_default_int(settings, 'hours', 3)

# def script_tick(seconds):
# 	obs.script_log(obs.LOG_INFO, f'{seconds} OBS 就要無法回應了！！！')
     
# 腳本計時器的回呼函式 welcome
def welcome():
    obs.script_log(obs.LOG_INFO, f'{type(obs.timer_add)}')
    obs.script_log(obs.LOG_INFO, '這是只被呼叫一次的回呼函式')
    # 移除 welcome 對應的腳本計時器
    obs.remove_current_callback()

# 加入腳本計時器，觸發時間間隔為 3 秒
obs.timer_add(welcome, 3000)