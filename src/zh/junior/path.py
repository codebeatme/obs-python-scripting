'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/get-script-path/ 如何获取脚本路径
'''

# 导入模块 obspython
import obspython as obs

def script_load(settings):
    # 不能使用 obs.script_path()
    current_path = script_path()

    obs.script_log(obs.LOG_INFO, f'脚本所在的文件夹路径：{current_path}')

# ERROR 此时 script_path 还没有被 OBS 定义
# script_path()