# 匯入模組 obspython
import obspython as obs

def test(props, prop):
    # 取得名稱為 OS 的擷取音訊輸入
    audio = obs.obs_get_source_by_name('OS')
    # 將擷取音訊輸入的音量設定為 0.5
    obs.obs_source_set_volume(audio, 0.5)

    # 如果擷取音訊輸入處於靜音狀態，則取消該狀態
    if obs.obs_source_muted(audio):
        obs.obs_source_set_muted(audio, False)

    # 關閉對擷取音訊輸入的監測
    obs.obs_source_set_monitoring_type(audio, obs.OBS_MONITORING_TYPE_NONE)

    # 如果擷取音訊輸入沒有輸出至第 1 條音軌，則新增
    mixers = obs.obs_source_get_audio_mixers(audio)
    if mixers & (1 << 0) != 1:
        obs.obs_source_set_audio_mixers(audio, mixers | (1 << 0))

    # 啟用擷取音訊輸入的按住靜音，並設定延遲時間
    obs.obs_source_enable_push_to_mute(audio, True)
    obs.obs_source_set_push_to_mute_delay(audio, 2000)
    
    # 釋放來源物件
    obs.obs_source_release(audio)

    # 取得名稱為 Media 的媒體來源
    media = obs.obs_get_source_by_name('Media')
    # 取得持續時間和目前時間，並計算播放進度
    duration = obs.obs_source_media_get_duration(media)
    time = obs.obs_source_media_get_time(media)
    obs.script_log(obs.LOG_INFO, f'Media 播放進度 {int(time * 100 / duration)}%')

    # 切換媒體來源的各種狀態
    state = obs.obs_source_media_get_state(media)
    if state == obs.OBS_MEDIA_STATE_PLAYING:
        obs.obs_source_media_play_pause(media, True)
    elif state == obs.OBS_MEDIA_STATE_PAUSED:
        obs.obs_source_media_play_pause(media, False)
    elif state == obs.OBS_MEDIA_STATE_STOPPED or state == obs.OBS_MEDIA_STATE_ENDED:
        obs.obs_source_media_restart(media)

    # 釋放來源物件
    obs.obs_source_release(media)

# 為腳本新增一個用於測試的按鈕，回呼函式為 test
def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(props, 'test', '測試', test)
    return props
