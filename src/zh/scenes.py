# 导入模块 obspython
import obspython as obs

def test(props, prop):
    # 创建一个名称为 sub_scene 的私有场景
    scene_sub = obs.obs_scene_create_private('scene_sub')
    # 获取场景 Scene 对应的场景对象
    source_scene = obs.obs_get_source_by_name('Scene')
    scene = obs.obs_scene_from_source(source_scene)
    # 将私有场景 sub_scene 添加至场景 Scene
    obs.obs_scene_add(scene, obs.obs_scene_get_source(scene_sub))

    # 创建一个文字（GDI+）来源
    settings = obs.obs_data_create_from_json('{"text":"新消息"}')
    source_text = obs.obs_source_create_private('text_gdiplus_v2', 'message', settings)
    # 将文字（GDI+）添加至场景 scene_sub
    obs.obs_scene_add(scene_sub, source_text)

    # 释放来源对象和来源设置对象
    obs.obs_source_release(source_text)
    obs.obs_data_release(settings)

    # 两次查找场景项 Welcome，第二次包括分组
    welcome = obs.obs_scene_find_source(scene, 'Welcome')
    obs.script_log(obs.LOG_INFO, f"找到了 Welcome？{welcome != None}")
    welcome = obs.obs_scene_find_source_recursive(scene, 'Welcome')
    obs.script_log(obs.LOG_INFO, f"找到了 Welcome（包括分组中的）？{welcome != None}")

    # 释放场景对象和来源对象
    obs.obs_source_release(source_scene)
    obs.obs_scene_release(scene_sub)

    # 将场景 Scene 复制为场景 Game，如果场景 Game 不存在
    source_game = obs.obs_get_source_by_name('Game')
    if not source_game:
        scene_game = obs.obs_scene_duplicate(scene, 'Game', obs.OBS_SCENE_DUP_REFS)
        # 释放场景对象
        obs.obs_scene_release(scene_game)
    else:
        # 释放来源对象
        obs.obs_source_release(source_game)

    # 在移除场景 World 之后，尝试移除不再使用的其他来源
    source_world = obs.obs_get_source_by_name('World')
    scene_world = obs.obs_scene_from_source(source_world)
    obs.obs_source_remove(source_world)
    obs.obs_scene_prune_sources(scene_world)
    obs.obs_source_release(source_world)

# 为脚本添加一个用于测试的按钮，回调函数为 test
def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(props, 'test', '测试', test)
    return props
