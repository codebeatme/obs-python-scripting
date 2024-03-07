'''
本節文章
https://learnscript.net/zh-hant/obs-python-scripting/junior/add-and-run-scripts/ 如何新增和執行腳本
'''

# 匯入模組 obspython
import obspython as obs

# 在指令稿記錄視窗顯示 Python 模組搜尋路徑
import sys
obs.script_log(obs.LOG_INFO, str(sys.path))