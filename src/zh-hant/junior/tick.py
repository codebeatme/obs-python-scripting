'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/script-function-exports/script-tick/ 腳本 Tick
'''

# 匯入模組 obspython，datetime
import obspython as obs
import datetime

# 記錄當前是一分鐘時間的第幾秒
current_second = -1
# 當前秒的總影格數
frame_count = 0
# 是否是第一個統計影格數的秒
first_second = True

def script_tick(seconds):
    # 函式 script_tick 會在 OBS 繪製每一影格時被呼叫
    global current_second, frame_count, first_second

    # 取得當前時間是第幾秒
    sec = datetime.datetime.now().second

    # 如果進入了新的一秒，則顯示上一秒的影格數資訊
    if sec != current_second:

        # 第一次執行時 sec 和 current_second 一定不相等，因此不能顯示資訊
        if current_second != -1:

            # 第一個開始統計的秒，其統計的影格數可能不全，因此也不給與顯示
            if first_second:
                first_second = False
            else:
                obs.script_log(obs.LOG_INFO, f'{frame_count} 影格/秒')

        current_second = sec
        frame_count = 0

    frame_count += 1