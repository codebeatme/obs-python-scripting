'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/script-properties/get-properties/ 如何取得屬性
'''

# 匯入模組 obspython，datetime
import obspython as obs
import datetime

props = None


def script_properties():
    # 為腳本添加屬性
    global props
    props = obs.obs_properties_create()

    # 計算當前是當周日次
    day = datetime.datetime.now().weekday() + 1

    # 添加一個核取方塊，用來提醒自己是否需要串流，當然該功能並沒有真的實作
    obs.obs_properties_add_bool(props, 'live', f'周 {day} 串流？')

    return props


def script_update(settings):
    # 當腳本更新時，顯示核取方塊的相關狀態
	# 使用 obs_properties_get 取得核取方塊相應的屬性
    prop = obs.obs_properties_get(props, 'live')

    if prop:
        # 取得核取方塊的說明
        description = obs.obs_property_description(prop)

        # 取得腳本設定項 live，他表示核取方塊是否處於已選取狀態
        live = obs.obs_data_get_bool(settings, 'live')
        obs.script_log(obs.LOG_INFO, f'{description}{live}')