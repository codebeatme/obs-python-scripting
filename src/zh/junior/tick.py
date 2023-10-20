'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/script-function-exports/script-tick/ 脚本 Tick
'''

# 导入模块 obspython，datetime
import obspython as obs
import datetime

# 记录当前是一分钟时间的第几秒
current_second = -1
# 当前秒的总帧数
frame_count = 0
# 是否是第一个统计帧数的秒
first_second = True

def script_tick(seconds):
    # 函数 script_tick 会在 OBS 绘制每一帧时被调用
    global current_second, frame_count, first_second

    # 获取当前时间是第几秒
    sec = datetime.datetime.now().second

    # 如果进入了新的一秒，则显示上一秒的帧数信息
    if sec != current_second:

        # 第一次执行时 sec 和 current_second 一定不相等，因此不能显示信息
        if current_second != -1:

            # 第一个开始统计的秒，其统计的帧数可能不全，因此也不给与显示
            if first_second:
                first_second = False
            else:
                obs.script_log(obs.LOG_INFO, f'{frame_count} 帧/秒')

        current_second = sec
        frame_count = 0

    frame_count += 1