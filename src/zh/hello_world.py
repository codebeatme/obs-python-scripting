'''
本节文章
https://learnscript.net/zh/obs-python-scripting/junior/add-and-run-scripts/ 如何添加和运行脚本
'''

# 导入模块 obspython
import obspython as obs

# 在脚本日志窗口显示 Python 模块搜索路径
import sys
obs.script_log(obs.LOG_INFO, str(sys.path))

def script_description():
    # 函数 script_description 用于提供脚本说明
    return ['12323sdfsdf','12323']