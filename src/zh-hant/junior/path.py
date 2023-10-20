'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/get-script-path/ 如何取得腳本路徑
'''

# 匯入模組 obspython
import obspython as obs

def script_load(settings):
    # 不能使用 obs.script_path()
    current_path = script_path()

    obs.script_log(obs.LOG_INFO, f'腳本所在的資料夾路徑：{current_path}')

# ERROR 此時 script_path 還沒有被 OBS 定義
# script_path()