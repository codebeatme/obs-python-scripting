# 匯入模組 obspython
import obspython as obs

def test(props, prop):
    # 取得文字（GDI+）來源中名稱為 blue 濾鏡
    welcome = obs.obs_get_source_by_name('Welcome')
    blue = obs.obs_source_get_filter_by_name(welcome, 'blue')

    if not blue:
        # 如果 blue 濾鏡不存在，則建立新增該濾鏡
        settings = obs.obs_data_create_from_json('{"color_multiply":' + str(0xFF0000) + '}')
        blue = obs.obs_source_create('color_filter_v2', 'blue', settings, None)
        obs.obs_source_filter_add(welcome, blue)

        # 取得來源的濾鏡個數，並將 blue 濾鏡移動至第二的位置
        count = obs.obs_source_filter_count(welcome)
        if count > 1:
            obs.obs_source_filter_set_index(welcome, blue, count - 2)

        # 釋放 OBS 資料設定物件
        obs.obs_data_release(settings)

    # 複製 Welcome 中的濾鏡到 Bye
    bye = obs.obs_get_source_by_name('Bye')
    obs.obs_source_copy_filters(bye, welcome)
    # 釋放 OBS 來源物件
    obs.obs_source_release(bye)

    # 釋放 OBS 來源物件
    obs.obs_source_release(blue)
    obs.obs_source_release(welcome)

    # 取得來源 Welcome 的隱藏轉場特效
    t = obs.obs_get_transition_by_name('Welcome 隱藏轉場特效')
    obs.obs_source_release(t)

# 為腳本新增一個用於測試的按鈕，回呼函式為 test
def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(props, 'test', '測試', test)
    return props
