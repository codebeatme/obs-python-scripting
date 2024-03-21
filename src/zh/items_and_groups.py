# 导入模块 obspython 和 vec2
import obspython as obs
from obspython import vec2

def test(props, prop):
    # 获取场景 Scene 对应的场景对象
    source_scene = obs.obs_get_source_by_name('Scene')
    scene = obs.obs_scene_from_source(source_scene)

    # 两次查找场景项 Welcome，第二次包括分组
    welcome = obs.obs_scene_find_source(scene, 'Welcome')
    obs.script_log(obs.LOG_INFO, f'找到了 Welcome？{welcome != None}')
    welcome = obs.obs_scene_find_source_recursive(scene, 'Welcome')
    obs.script_log(obs.LOG_INFO, f'找到了 Welcome（包括分组中的）？{welcome != None}')

    # 显示场景项 Welcome 的来源类型标识符
    source_welcome = obs.obs_sceneitem_get_source(welcome)
    obs.script_log(obs.LOG_INFO, f'{obs.obs_source_get_unversioned_id(source_welcome)}')

    # 将场景项 Welcome 移除
    obs.obs_sceneitem_remove(welcome)

    # 将场景项 Hi 移动至末尾
    hi = obs.obs_scene_find_source(scene, 'Hi')
    obs.obs_sceneitem_set_order_position(hi, 0)

    # 设置场景项 Hi 的位置
    pos = vec2()
    pos.x = 100
    pos.y = 100
    obs.obs_sceneitem_set_pos(hi, pos)
    # 设置场景项 Hi 的旋转角度
    obs.obs_sceneitem_set_rot(hi, 30)
    # 设置场景项 Hi 的缩放
    scale = vec2()
    scale.x = 1.5
    scale.y = 1.5
    obs.obs_sceneitem_set_scale(hi, scale)

    # 保存并加载场景项的变换信息，使中途的修改无效
    states = obs.obs_scene_save_transform_states(scene, True)
    # 设置场景项 Hi 的旋转角度
    obs.obs_sceneitem_set_rot(hi, 90)
    obs.obs_scene_load_transform_states(obs.obs_data_get_json(states))

    # 为场景项 Hi 增加滑出的隐藏转场效果
    transition = obs.obs_source_create('swipe_transition', 'hi_hide_transition', None, None)
    obs.obs_sceneitem_set_transition(hi, False, transition)
    obs.obs_sceneitem_do_transition(hi, False)
    # 释放来源对象
    obs.obs_source_release(transition)

    # 创建一个新的分组，并将 Hi 加入其中
    message = obs.obs_scene_add_group(scene, 'Message')
    obs.obs_sceneitem_group_add_item(message, hi)

    # 获取场景项 Bye 所在的分组
    bye = obs.obs_scene_find_source_recursive(scene, 'Bye')
    group = obs.obs_sceneitem_get_group(scene, bye)
    obs.script_log(obs.LOG_INFO, f'是分组？{obs.obs_sceneitem_is_group(group)}')

    # 释放来源对象
    obs.obs_source_release(source_scene)

# 为脚本添加一个用于测试的按钮，回调函数为 test
def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(props, 'test', '测试', test)
    return props
