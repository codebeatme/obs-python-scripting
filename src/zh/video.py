# 导入模块 obspython
import obspython as obs

def test(props, prop):
    audio = obs.obs_get_source_by_name('A')
    obs.script_log(obs.LOG_INFO, f"obs_source_get_volume {obs.obs_source_get_volume(audio)}")
    obs.script_log(obs.LOG_INFO, f"obs_source_muted {obs.obs_source_muted(audio)}")
    obs.script_log(obs.LOG_INFO, f"obs_source_get_balance_value {obs.obs_source_get_balance_value(audio)}")
    obs.script_log(obs.LOG_INFO, f"obs_source_get_sync_offset {obs.obs_source_get_sync_offset(audio)}")
    obs.script_log(obs.LOG_INFO, f"obs_source_get_audio_mixers {obs.obs_source_get_audio_mixers(audio)}")
    obs.script_log(obs.LOG_INFO, f"obs_source_get_monitoring_type {obs.obs_source_get_monitoring_type(audio)}")

# 为脚本添加一个用于测试的按钮，回调函数为 test
def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(props, 'test', '测试', test)
    return props
