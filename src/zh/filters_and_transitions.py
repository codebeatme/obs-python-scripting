# 导入模块 obspython
import obspython as obs

def test(props, prop):
    # 获取文字（GDI+）来源中名称为 blue 滤镜
    welcome = obs.obs_get_source_by_name('Welcome')
    blue = obs.obs_source_get_filter_by_name(welcome, 'blue')

    if not blue:
        # 如果 blue 滤镜不存在，则创建添加该滤镜
        settings = obs.obs_data_create_from_json('{"color_multiply":' + str(0xFF0000) + '}')
        blue = obs.obs_source_create('color_filter_v2', 'blue', settings, None)
        obs.obs_source_filter_add(welcome, blue)

        # 获取来源的滤镜个数，并将 blue 滤镜移动至第二的位置
        count = obs.obs_source_filter_count(welcome)
        if count > 1:
            obs.obs_source_filter_set_index(welcome, blue, count - 2)

        # 释放 OBS 数据设置对象
        obs.obs_data_release(settings)

    # 复制 Welcome 中的滤镜到 Bye
    bye = obs.obs_get_source_by_name('Bye')
    obs.obs_source_copy_filters(bye, welcome)
    # 释放 OBS 来源对象
    obs.obs_source_release(bye)

    # 释放 OBS 来源对象
    obs.obs_source_release(blue)
    obs.obs_source_release(welcome)

    # 获取来源 Welcome 的隐藏转场特效
    t = obs.obs_get_transition_by_name('Welcome 隐藏转场特效')
    obs.obs_source_release(t)

# 为脚本添加一个用于测试的按钮，回调函数为 test
def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(props, 'test', '测试', test)
    return props
