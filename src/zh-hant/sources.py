# 匯入模組 obspython
import obspython as obs

def test(props, prop):
    # 建立一個名稱為 my_text 的文字（GDI+）來源，並將字串 "今天天氣不錯！" 設定為文字
    settings = obs.obs_data_create_from_json('{"text":"今天天氣不錯！"}')
    source_text = obs.obs_source_create('text_gdiplus', 'my_text', settings, None)

    # 將文字（GDI+）來源，新增至名為 Scene 的場景
    source_scene = obs.obs_get_source_by_name('Scene')
    scene = obs.obs_scene_from_source(source_scene)
    obs.obs_scene_add(scene, source_text)

    # 釋放來源物件和來源設定物件
    obs.obs_source_release(source_scene)
    obs.obs_source_release(source_text)
    obs.obs_data_release(settings)

    # 複製名稱為 Welcome 的來源，並指定新名稱 Bye
    welcome = obs.obs_get_source_by_name('Welcome')
    bye = obs.obs_source_duplicate(welcome, 'Bye', False)

    # 通過 Welcome 的來源設定物件，修改其對應的文字
    settings = obs.obs_source_get_settings(welcome)
    obs.obs_data_set_string(settings, 'text', '你好，歡迎！')
    obs.obs_source_update(welcome, settings)
    # 釋放來源設定物件
    obs.obs_data_release(settings)

    # 顯示 Weclome 來源的大小
    width = obs.obs_source_get_width(welcome)
    height = obs.obs_source_get_height(welcome)
    obs.script_log(obs.LOG_INFO, f"Welcome 的大小 {width}x{height}")

    # 顯示 Weclome 來源的來源類型識別碼和 UUID
    v_id = obs.obs_source_get_id(welcome)
    id = obs.obs_source_get_unversioned_id(welcome)
    obs.script_log(obs.LOG_INFO, f"Welcome 的 id {v_id} {id}")
    uuid = obs.obs_source_get_uuid(welcome)
    obs.script_log(obs.LOG_INFO, f"Welcome 的 uuid {uuid}")

    # 釋放來源 Welcome 和 Bye
    obs.obs_source_release(welcome)
    obs.obs_source_release(bye)

    # 如果存在名稱為 Groups 的來源，則將其改名為 Group
    groups = obs.obs_get_source_by_name('Groups')
    if groups:
        obs.obs_source_set_name(groups, 'Group')
        obs.obs_source_release(groups)

    # 顯示 Group 來源的類型，並判斷是否為群組
    group = obs.obs_get_source_by_name('Group')
    group_type = obs.obs_source_get_type(group)
    obs.script_log(obs.LOG_INFO, f"Group 的類型 {group_type}，等於 OBS_SOURCE_TYPE_SCENE？{group_type == obs.OBS_SOURCE_TYPE_SCENE}")
    obs.script_log(obs.LOG_INFO, f"Group 是群組？{obs.obs_source_is_group(group)}")
    obs.obs_source_release(group)

    # 來源 Screen 如果存在，則將其移除
    screen = obs.obs_get_source_by_name('Screen')
    if screen:
        obs.obs_source_remove(screen)
        obs.script_log(obs.LOG_INFO, f"Screen 被移除？{obs.obs_source_removed(screen)}")
        obs.obs_source_release(screen)

    # 判斷來源 Video 的輸出旗標
    video = obs.obs_get_source_by_name('Video')
    flags = obs.obs_source_get_output_flags(video)
    obs.script_log(obs.LOG_INFO, f"Video 具有視訊功能？{flags & obs.OBS_SOURCE_VIDEO == obs.OBS_SOURCE_VIDEO}")
    obs.script_log(obs.LOG_INFO, f"Video 具有音訊功能？{flags & obs.OBS_SOURCE_AUDIO == obs.OBS_SOURCE_AUDIO}")
    obs.obs_source_release(video)

# 為腳本新增一個用於測試的按鈕，回呼函式為 test
def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(props, 'test', '測試', test)
    return props


# def script_update(settings):
#     # 複製名稱為 Welcome 的來源，並指定新名稱 Bye
#     welcome = obs.obs_get_source_by_name('Welcome')
#     bye = obs.obs_source_duplicate(welcome, 'Bye', False)

#     # 通過 Welcome 的來源設定物件，修改其對應的文字
#     settings = obs.obs_source_get_settings(welcome)
#     obs.obs_data_set_string(settings, 'text', '你好，歡迎！')
#     obs.obs_source_update(welcome, settings)
#     # 釋放來源設定物件
#     obs.obs_data_release(settings)

#     obs.script_log(obs.LOG_INFO, f"{obs.obs_source_get_width(welcome)} {obs.obs_source_get_width(welcome)}")

#     # 釋放來源 Welcome 和 Bye
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
