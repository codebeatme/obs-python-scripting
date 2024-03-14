# 导入模块 obspython
import obspython as obs

def test(props, prop):
    # 创建一个名称为 my_text 的文本（GDI+）来源，并将字符串 "今天天气不错！" 设置为文本
    settings = obs.obs_data_create_from_json('{"text":"今天天气不错！"}')
    source_text = obs.obs_source_create('text_gdiplus', 'my_text', settings, None)

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


# def script_update(settings):
#     # 复制名称为 Welcome 的来源，并指定新名称 Bye
#     welcome = obs.obs_get_source_by_name('Welcome')
#     bye = obs.obs_source_duplicate(welcome, 'Bye', False)

#     # 通过 Welcome 的来源设置对象，修改其对应的文本
#     settings = obs.obs_source_get_settings(welcome)
#     obs.obs_data_set_string(settings, 'text', '你好，欢迎！')
#     obs.obs_source_update(welcome, settings)
#     # 释放来源设置对象
#     obs.obs_data_release(settings)

#     obs.script_log(obs.LOG_INFO, f"{obs.obs_source_get_width(welcome)} {obs.obs_source_get_width(welcome)}")

#     # 释放来源 Welcome 和 Bye
#     obs.obs_source_release(welcome)
#     obs.obs_source_release(bye)

# obs.script_log(obs.LOG_INFO, f"{obs.obs_source_get_display_name('text_gdiplus')}")
# obs.script_log(obs.LOG_INFO, f"{obs.obs_source_get_display_name('color_filter')}")

# o = obs.obs_source_create_private("text_gdiplus", "my_test", None)
# obs.script_log(obs.LOG_INFO, f" my_test {obs.obs_source_is_hidden(o)}")
# obs.script_log(obs.LOG_INFO, f"{obs.obs_source_get_name(o)} {obs.obs_source_removed(o)}")
# obs.obs_source_release(o)
# o2 = obs.obs_source_create("text_gdiplus", "my_test", None, None)
# obs.script_log(obs.LOG_INFO, f"{obs.obs_source_get_name(o2)}")

# o = obs.obs_get_source_by_name('圖片')
# if o:
#     # obs.script_log(obs.LOG_INFO, f"{obs.obs_get_source_by_name('圖片')}")
#     o1 = obs.obs_source_duplicate(o, 'None', False)
#     obs.obs_source_release(o)
#     obs.obs_source_release(o1)

#     v = obs.obs_source_is_hidden(o)
#     obs.obs_source_set_hidden(o, True)
#     obs.script_log(obs.LOG_INFO, f"hidden {v}")

# o = obs.obs_get_source_by_name('場景 2 2')
# # o1 = obs.obs_get_source_by_name('Welcome')
# if o:
#     # # obs.obs_source_remove(o)
#     # # obs.script_log(obs.LOG_INFO, f"{obs.obs_source_removed(o1)}")
#     # # obs.obs_source_release(o)
#     # abc = obs.obs_source_get_id(o)
#     # obs.script_log(obs.LOG_INFO, f"{obs.obs_source_get_output_flags(o)}x{abc}x{obs.obs_get_source_output_flags(abc)}")
#     # obs.script_log(obs.LOG_INFO, f"{obs.OBS_SOURCE_TYPE_INPUT}x{obs.OBS_SOURCE_TYPE_FILTER}x{obs.OBS_SOURCE_TYPE_TRANSITION}x{obs.OBS_SOURCE_TYPE_SCENE}")
#     # # obs.obs_source_set_name(o, '場景 2')
#     s = obs.obs_source_get_settings(o)
#     json = obs.obs_data_get_json(s)
#     obs.script_log(obs.LOG_INFO, f"{json}")
#     obs.script_log(obs.LOG_INFO, f"{obs.obs_data_get_string(s, 'text')}")

#     obs.obs_data_set_string(s, 'text', '你好哦！')
#     obs.obs_source_update(o, s)
#     obs.obs_data_release(s)
#     obs.obs_data_release(s)
#     obs.script_log(obs.LOG_INFO, f"text re={obs.obs_data_get_string(s, 'text')}")
#     obs.obs_source_release(o)

# o = obs.obs_get_source_by_name('場景 2 2')
# # o1 = obs.obs_get_source_by_name('Welcome')
# if o:
#     obs.script_log(obs.LOG_INFO, f"{obs.obs_source_showing(o)}")
#     obs.obs_source_dec_showing(o)
#     obs.obs_source_set_enabled(o, True)
#     obs.script_log(obs.LOG_INFO, f"{obs.obs_source_showing(o)}")
#     obs.obs_source_release(o)

# d4 = obs.obs_get_source_defaults('text_gdiplus')
# obs.obs_data_release(d4)
# obs.obs_data_release(d4)
# d4 = obs.obs_get_source_defaults('text_gdiplus')
# obs.script_log(obs.LOG_INFO, obs.obs_data_get_string(d4, 'align'))

# d = obs.obs_data_create()

# do = obs.obs_data_array_create()

# obs.obs_data_set_default_array(d, "player", do)

# i = obs.obs_data_create()
# obs.obs_data_array_push_back(do, i)
# obs.obs_data_release(i)
# obs.obs_data_array_release(do)

# do = obs.obs_data_get_default_array(d, "player")
# # do = obs.obs_data_get_default_array(d, "player")
# obs.script_log(obs.LOG_INFO, f"count def={obs.obs_data_array_count(do)}")
# obs.obs_data_array_release(do)
# # obs.obs_data_array_release(do)
# do = obs.obs_data_get_default_array(d, "player")
# obs.script_log(obs.LOG_INFO, f"count released def={obs.obs_data_array_count(do)}")

# de = obs.obs_data_get_defaults(d)

# obs.script_log(obs.LOG_INFO, f"name def={obs.obs_data_get_string(de, 'name')}")
# obs.script_log(obs.LOG_INFO, f"age def={obs.obs_data_get_string(de, 'age')}")

# # obs.obs_data_release(de)
# obs.obs_data_release(d)

# obs.script_log(obs.LOG_INFO, f"name def={obs.obs_data_get_string(d, 'name')}")
# obs.script_log(obs.LOG_INFO, f"age def={obs.obs_data_get_string(d, 'age')}")

# def call(p, c, pa):
#     pass

# o = obs.obs_get_source_by_name('場景 2 2')
# # o1 = obs.obs_get_source_by_name('Welcome')
# if o:
#     obs.script_log(obs.LOG_INFO, f"{obs.obs_source_showing(o)}")
#     # c = obs.obs_source_create("color_key_filter", "my_test111", None, None)
#     # obs.obs_source_add_active_child(o, c)
#     # obs.obs_source_release(c)
#     props = obs.obs_source_properties(o)
#     p = obs.obs_properties_first(props)
#     obs.obs_property_set_enabled(p, False)
#     obs.obs_source_update_properties(o)
#     obs.obs_source_release(o)
