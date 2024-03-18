# 匯入模組 obspython
import obspython as obs

def test(props, prop):
    # 建立一個名稱為 sub_scene 的私用場景
    scene_sub = obs.obs_scene_create_private('scene_sub')
    # 取得場景 Scene 對應的場景物件
    source_scene = obs.obs_get_source_by_name('Scene')
    scene = obs.obs_scene_from_source(source_scene)
    # 將私用場景 sub_scene 新增至場景 Scene
    obs.obs_scene_add(scene, obs.obs_scene_get_source(scene_sub))

    # 建立一個文字（GDI+）來源
    settings = obs.obs_data_create_from_json('{"text":"新訊息"}')
    source_text = obs.obs_source_create_private('text_gdiplus_v2', 'message', settings)
    # 將文字（GDI+）新增至場景 scene_sub
    obs.obs_scene_add(scene_sub, source_text)

    # 釋放來源物件和來源設定物件
    obs.obs_source_release(source_text)
    obs.obs_data_release(settings)

    # 兩次尋找場景項 Welcome，第二次包括群組
    welcome = obs.obs_scene_find_source(scene, 'Welcome')
    obs.script_log(obs.LOG_INFO, f"找到了 Welcome？{welcome != None}")
    welcome = obs.obs_scene_find_source_recursive(scene, 'Welcome')
    obs.script_log(obs.LOG_INFO, f"找到了 Welcome（包括群組中的）？{welcome != None}")

    # 釋放場景物件和來源物件
    obs.obs_source_release(source_scene)
    obs.obs_scene_release(scene_sub)

    # 將場景 Scene 複製為場景 Game，如果場景 Game 不存在
    source_game = obs.obs_get_source_by_name('Game')
    if not source_game:
        scene_game = obs.obs_scene_duplicate(scene, 'Game', obs.OBS_SCENE_DUP_REFS)
        # 釋放場景物件
        obs.obs_scene_release(scene_game)
    else:
        # 釋放來源物件
        obs.obs_source_release(source_game)

    # 在移除場景 World 之後，嘗試移除不再使用的其他來源
    source_world = obs.obs_get_source_by_name('World')
    scene_world = obs.obs_scene_from_source(source_world)
    obs.obs_source_remove(source_world)
    obs.obs_scene_prune_sources(scene_world)
    obs.obs_source_release(source_world)

# 為腳本新增一個用於測試的按鈕，回呼函式為 test
def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(props, 'test', '測試', test)
    return props
