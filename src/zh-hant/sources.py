# 匯入模組 obspython
import obspython as obs

def test(props, prop):
    # 建立一個名稱為 my_text 的私用文字（GDI+）來源，並將字串 "今天天氣不錯！" 設定為文字
    settings = obs.obs_data_create_from_json('{"text":"今天天氣不錯！"}')
    source_text = obs.obs_source_create_private('text_gdiplus', 'my_text', settings)

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
    obs.script_log(obs.LOG_INFO, f'Welcome 的大小 {width}x{height}')

    # 顯示 Weclome 來源的來源類型識別碼和 UUID
    v_id = obs.obs_source_get_id(welcome)
    id = obs.obs_source_get_unversioned_id(welcome)
    obs.script_log(obs.LOG_INFO, f'Welcome 的 id {v_id} {id}')
    uuid = obs.obs_source_get_uuid(welcome)
    obs.script_log(obs.LOG_INFO, f'Welcome 的 uuid {uuid}')

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
    obs.script_log(obs.LOG_INFO, f'Group 的類型 {group_type}，等於 OBS_SOURCE_TYPE_SCENE？{group_type == obs.OBS_SOURCE_TYPE_SCENE}')
    obs.script_log(obs.LOG_INFO, f'Group 是群組？{obs.obs_source_is_group(group)}')
    obs.obs_source_release(group)

    # 來源 Screen 如果存在，則將其移除
    screen = obs.obs_get_source_by_name('Screen')
    if screen:
        obs.obs_source_remove(screen)
        obs.script_log(obs.LOG_INFO, f'Screen 被移除？{obs.obs_source_removed(screen)}')
        obs.obs_source_release(screen)

    # 判斷來源 Video 的輸出旗標
    video = obs.obs_get_source_by_name('Video')
    flags = obs.obs_source_get_output_flags(video)
    obs.script_log(obs.LOG_INFO, f'Video 具有視訊功能？{flags & obs.OBS_SOURCE_VIDEO == obs.OBS_SOURCE_VIDEO}')
    obs.script_log(obs.LOG_INFO, f'Video 具有音訊功能？{flags & obs.OBS_SOURCE_AUDIO == obs.OBS_SOURCE_AUDIO}')
    obs.obs_source_release(video)

# 為腳本新增一個用於測試的按鈕，回呼函式為 test
def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(props, 'test', '測試', test)
    return props
