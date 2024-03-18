# 导入模块 obspython
import obspython as obs

def test(props, prop):
    # 获取名称为 OS 的音频输入采集
    audio = obs.obs_get_source_by_name('OS')
    # 将音频输入采集的音量设置为 0.5
    obs.obs_source_set_volume(audio, 0.5)

    # 如果音频输入采集处于静音状态，则取消该状态
    if obs.obs_source_muted(audio):
        obs.obs_source_set_muted(audio, False)

    # 关闭对音频输入采集的监听
    obs.obs_source_set_monitoring_type(audio, obs.OBS_MONITORING_TYPE_NONE)

    # 如果音频输入采集没有输出至第 1 条音轨，则添加
    mixers = obs.obs_source_get_audio_mixers(audio)
    if mixers & (1 << 0) != 1:
        obs.obs_source_set_audio_mixers(audio, mixers | (1 << 0))

    # 启用音频输入采集的按住静音，并设置延迟时间
    obs.obs_source_enable_push_to_mute(audio, True)
    obs.obs_source_set_push_to_mute_delay(audio, 2000)
    
    # 释放来源对象
    obs.obs_source_release(audio)

    # 获取名称为 Media 的媒体源
    media = obs.obs_get_source_by_name('Media')
    # 获取持续时间和当前时间，并计算播放进度
    duration = obs.obs_source_media_get_duration(media)
    time = obs.obs_source_media_get_time(media)
    obs.script_log(obs.LOG_INFO, f"Media 播放进度 {int(time * 100 / duration)}%")

    # 切换媒体源的各种状态
    state = obs.obs_source_media_get_state(media)
    if state == obs.OBS_MEDIA_STATE_PLAYING:
        obs.obs_source_media_play_pause(media, True)
    elif state == obs.OBS_MEDIA_STATE_PAUSED:
        obs.obs_source_media_play_pause(media, False)
    elif state == obs.OBS_MEDIA_STATE_STOPPED or state == obs.OBS_MEDIA_STATE_ENDED:
        obs.obs_source_media_restart(media)

    # 释放来源对象
    obs.obs_source_release(media)

# 为脚本添加一个用于测试的按钮，回调函数为 test
def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(props, 'test', '测试', test)
    return props
