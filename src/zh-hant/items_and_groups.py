# 匯入模組 obspython 和 vec2
import obspython as obs
from obspython import vec2

def test(props, prop):
    # 取得場景 Scene 對應的場景物件
    source_scene = obs.obs_get_source_by_name('Scene')
    scene = obs.obs_scene_from_source(source_scene)

    # 兩次尋找場景項 Welcome，第二次包括群組
    welcome = obs.obs_scene_find_source(scene, 'Welcome')
    obs.script_log(obs.LOG_INFO, f'找到了 Welcome？{welcome != None}')
    welcome = obs.obs_scene_find_source_recursive(scene, 'Welcome')
    obs.script_log(obs.LOG_INFO, f'找到了 Welcome（包括群組中的）？{welcome != None}')

    # 顯示場景項 Welcome 的來源類型識別碼
    source_welcome = obs.obs_sceneitem_get_source(welcome)
    obs.script_log(obs.LOG_INFO, f'{obs.obs_source_get_unversioned_id(source_welcome)}')

    # 將場景項 Welcome 移除
    obs.obs_sceneitem_remove(welcome)

    # 將場景項 Hi 移動至末尾
    hi = obs.obs_scene_find_source(scene, 'Hi')
    obs.obs_sceneitem_set_order_position(hi, 0)

    # 設定場景項 Hi 的位置
    pos = vec2()
    pos.x = 100
    pos.y = 100
    obs.obs_sceneitem_set_pos(hi, pos)
    # 設定場景項 Hi 的旋轉角度
    obs.obs_sceneitem_set_rot(hi, 30)
    # 設定場景項 Hi 的縮放
    scale = vec2()
    scale.x = 1.5
    scale.y = 1.5
    obs.obs_sceneitem_set_scale(hi, scale)

    # 儲存並載入場景項的變型資訊，使中途的修改無效
    states = obs.obs_scene_save_transform_states(scene, True)
    # 設定場景項 Hi 的旋轉角度
    obs.obs_sceneitem_set_rot(hi, 90)
    obs.obs_scene_load_transform_states(obs.obs_data_get_json(states))
    # 釋放資料設定物件
    obs.obs_data_release(states)

    # 為場景項 Hi 增加滑出的隱藏轉場效果
    transition = obs.obs_source_create('swipe_transition', 'hi_hide_transition', None, None)
    obs.obs_sceneitem_set_transition(hi, False, transition)
    obs.obs_sceneitem_do_transition(hi, False)
    # 釋放來源物件
    obs.obs_source_release(transition)

    # 建立一個新的群組，並將 Hi 加入其中
    message = obs.obs_scene_add_group(scene, 'Message')
    obs.obs_sceneitem_group_add_item(message, hi)

    # 取得場景項 Bye 所在的群組
    bye = obs.obs_scene_find_source_recursive(scene, 'Bye')
    group = obs.obs_sceneitem_get_group(scene, bye)
    obs.script_log(obs.LOG_INFO, f'是群組？{obs.obs_sceneitem_is_group(group)}')

    # 釋放來源物件
    obs.obs_source_release(source_scene)

# 為腳本新增一個用於測試的按鈕，回呼函式為 test
def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(props, 'test', '測試', test)
    return props
