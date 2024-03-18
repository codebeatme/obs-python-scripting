# 导入模块 obspython
import obspython as obs

def test(props, prop):
    # 创建一个名称为 my_text 的私有文本（GDI+）来源，并将字符串 "今天天气不错！" 设置为文本
    settings = obs.obs_data_create_from_json('{"text":"今天天气不错！"}')
    source_text = obs.obs_source_create_private('text_gdiplus', 'my_text', settings)

    # 将文本（GDI+）来源，添加至名为 Scene 的场景
    source_scene = obs.obs_get_source_by_name('Scene')
    scene = obs.obs_scene_from_source(source_scene)
    obs.obs_scene_add(scene, source_text)

    # 释放来源对象和来源设置对象
    obs.obs_source_release(source_scene)
    obs.obs_source_release(source_text)
    obs.obs_data_release(settings)

    # 复制名称为 Welcome 的来源，并指定新名称 Bye
    welcome = obs.obs_get_source_by_name('Welcome')
    bye = obs.obs_source_duplicate(welcome, 'Bye', False)

    # 通过 Welcome 的来源设置对象，修改其对应的文本
    settings = obs.obs_source_get_settings(welcome)
    obs.obs_data_set_string(settings, 'text', '你好，欢迎！')
    obs.obs_source_update(welcome, settings)
    # 释放来源设置对象
    obs.obs_data_release(settings)

    # 显示 Weclome 来源的大小
    width = obs.obs_source_get_width(welcome)
    height = obs.obs_source_get_height(welcome)
    obs.script_log(obs.LOG_INFO, f"Welcome 的大小 {width}x{height}")

    # 显示 Weclome 来源的来源类型标识符和 UUID
    v_id = obs.obs_source_get_id(welcome)
    id = obs.obs_source_get_unversioned_id(welcome)
    obs.script_log(obs.LOG_INFO, f"Welcome 的 id {v_id} {id}")
    uuid = obs.obs_source_get_uuid(welcome)
    obs.script_log(obs.LOG_INFO, f"Welcome 的 uuid {uuid}")

    # 释放来源 Welcome 和 Bye
    obs.obs_source_release(welcome)
    obs.obs_source_release(bye)

    # 如果存在名称为 Groups 的来源，则将其改名为 Group
    groups = obs.obs_get_source_by_name('Groups')
    if groups:
        obs.obs_source_set_name(groups, 'Group')
        obs.obs_source_release(groups)

    # 显示 Group 来源的类型，并判断是否为分组
    group = obs.obs_get_source_by_name('Group')
    group_type = obs.obs_source_get_type(group)
    obs.script_log(obs.LOG_INFO, f"Group 的类型 {group_type}，等于 OBS_SOURCE_TYPE_SCENE？{group_type == obs.OBS_SOURCE_TYPE_SCENE}")
    obs.script_log(obs.LOG_INFO, f"Group 是分组？{obs.obs_source_is_group(group)}")
    obs.obs_source_release(group)

    # 来源 Screen 如果存在，则将其移除
    screen = obs.obs_get_source_by_name('Screen')
    if screen:
        obs.obs_source_remove(screen)
        obs.script_log(obs.LOG_INFO, f"Screen 被移除？{obs.obs_source_removed(screen)}")
        obs.obs_source_release(screen)

    # 判断来源 Video 的输出标志
    video = obs.obs_get_source_by_name('Video')
    flags = obs.obs_source_get_output_flags(video)
    obs.script_log(obs.LOG_INFO, f"Video 具有视频功能？{flags & obs.OBS_SOURCE_VIDEO == obs.OBS_SOURCE_VIDEO}")
    obs.script_log(obs.LOG_INFO, f"Video 具有音频功能？{flags & obs.OBS_SOURCE_AUDIO == obs.OBS_SOURCE_AUDIO}")
    obs.obs_source_release(video)

# 为脚本添加一个用于测试的按钮，回调函数为 test
def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(props, 'test', '测试', test)
    return props
