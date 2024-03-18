# 匯入模組 obspython
import obspython as obs

def test(props, prop):
    audio = obs.obs_get_source_by_name('MIC')
    obs.script_log(obs.LOG_INFO, f"obs_source_get_volume {obs.obs_source_get_volume(audio)}")
    obs.script_log(obs.LOG_INFO, f"obs_source_muted {obs.obs_source_muted(audio)}")
    obs.script_log(obs.LOG_INFO, f"obs_source_get_balance_value {obs.obs_source_get_balance_value(audio)}")
    obs.script_log(obs.LOG_INFO, f"obs_source_get_sync_offset {obs.obs_source_get_sync_offset(audio)}")
    obs.script_log(obs.LOG_INFO, f"obs_source_get_audio_mixers {obs.obs_source_get_audio_mixers(audio)}")
    obs.script_log(obs.LOG_INFO, f"obs_source_get_monitoring_type {obs.obs_source_get_monitoring_type(audio)}")
    obs.obs_source_set_volume(audio, 1)
    obs.obs_source_set_audio_mixers(audio, (1<<0)|(1<<5))

# 為腳本新增一個用於測試的按鈕，回呼函式為 test
def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(props, 'test', '測試', test)
    return props
