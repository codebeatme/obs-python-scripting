# 匯入模組 obspython
import obspython as obs


# 函式 load_message 將讀取文字檔案中的內容，並將其寫入文字方塊
def load_message(props, prop, settings):
    # 取得檔案對話方塊中的檔案路徑
    path = obs.obs_data_get_string(settings, 'more')

    if path:
        # 從檔案讀取內容
        file = open(path, 'r', encoding='utf-8')
        content = file.read()
        file.close()

        # 將內容設定到文字方塊中，如果內容與文字方塊不一致
        if content != obs.obs_data_get_string(settings, 'message'):
            obs.obs_data_set_string(settings, 'message', content)
            # 立即將腳本設定更新至控製項，這將導致 load_message 再次被呼叫
            obs.obs_properties_apply_settings(props, settings)
            # 這裏需要傳回特定值 True
            return True

# 函式 set_source_color 將色彩對話方塊指定的色彩，設定到文字來源
def set_source_color(settings):
    # 取得色彩對話方塊所確定的色彩
    color = obs.obs_data_get_int(settings, 'color')

    # 為場景中的文字來源 Welcome 設定色彩
    source = obs.obs_get_source_by_name('Welcome')
    data = obs.obs_data_create()
    obs.obs_data_set_int(data, 'color', color)
    obs.obs_source_update(source, data)
    obs.obs_data_release(data)
    obs.obs_source_release(source)

# 函式 set_source_font 將字型對話方塊指定的字型，設定到文字來源
def set_source_font(settings):
    # 取得字型對話方塊所確定的字型
    font = obs.obs_data_get_obj(settings, 'font')
    # obs.script_log(obs.LOG_INFO, f"色彩：{font}")
    
    # 為場景中的文字來源 Welcome 設定字型
    source = obs.obs_get_source_by_name('Welcome')
    data = obs.obs_data_create()
    obs.obs_data_set_obj(data, 'font', font)
    obs.obs_source_update(source, data)
    obs.obs_data_release(font)
    obs.obs_data_release(data)
    obs.obs_source_release(source)

# 函式 set_source_text 將隨機選擇清單方塊中的項，然後將其設定為文字來源的文字
def set_source_text(settings):
    # 取得清單方塊中的所有項
    my_texts = obs.obs_data_get_array(settings, 'my_texts')

    # 隨機選擇一個項，並將其內容設定為文字來源的文字
    count = obs.obs_data_array_count(my_texts)
    if count > 0:
        import random
        index = random.randint(0, count - 1)
        item = obs.obs_data_array_item(my_texts, index)

        # 設定場景中的文字來源 Welcome 的文字
        source = obs.obs_get_source_by_name('Welcome')
        data = obs.obs_data_create()
        obs.obs_data_set_string(data, 'text', obs.obs_data_get_string(item, 'value'))
        obs.obs_source_update(source, data)
        obs.obs_data_release(data)
        obs.obs_source_release(source)

# 用於登入的函式 login
def login(props, prop):
    # 點選登入按鈕後，將隱藏群組方塊
    group_login = obs.obs_properties_get(props, 'group_login')
    obs.obs_property_set_visible(group_login, False)
    # 這裏需要傳回特定值 True，否則無法看到隱藏效果
    return True

# 移除按鈕自身
def remove_myself(props, prop):
    obs.obs_properties_remove_by_name(props, 'remove')
    # 這裏需要傳回特定值 True
    return True

# 讓訊息文字方塊顯示隨機的文字
def set_random_text(props, prop):
    # 隨機的取得一個文字
    import random
    messages = ('天氣不錯！', '吃了嗎？', '下雨啦！')
    text = messages[random.randint(0, 2)]

    # 將隨機文字寫入設定項 message
    obs.obs_data_set_string(current_settings, 'message', text)
    # 將腳本設定應用到屬性集物件
    obs.obs_properties_apply_settings(props, current_settings)
    # 這裏需要傳回特定值 True
    return True

def script_properties():
    # 建立一個屬性集物件
    props = obs.obs_properties_create()

    # 新增一個核取方塊，用於控製是否在腳本載入後執行任務
    obs.obs_properties_add_bool(props, 'auto', '在啟動時執行任務？')
    # 新增一個小數滑桿，用於表示延遲執行任務的時間，尾碼為字串 '秒'
    delay = obs.obs_properties_add_float_slider(props, 'delay', '延遲秒數', 1, 10, 0.5)
    obs.obs_property_float_set_suffix(delay, '秒')
    # 新增一個文字方塊，用於表示需要傳送的訊息
    obs.obs_properties_add_text(props, 'message', '訊息：', obs.OBS_TEXT_MULTILINE)
    # 新增一個按鈕，用於再次執行 task 函式
    obs.obs_properties_add_button(props, 'again', '再次執行', lambda ps, p: task())

    # 新增一個下拉式方塊，用於選擇串流平臺
    platform = obs.obs_properties_add_list(props, 'platform', '串流平臺：', obs.OBS_COMBO_TYPE_LIST, obs.OBS_COMBO_FORMAT_STRING)
    # 為下拉式方塊新增項，需要給出項的名稱和值
    obs.obs_property_list_add_string(platform, 'YouTube', 'yt')
    obs.obs_property_list_add_string(platform, 'Twitch', 't')
    # 在下拉式方塊的第二個位置插入項，並使其不可用
    obs.obs_property_list_insert_string(platform, 1, 'Unkown', 'u')
    obs.obs_property_list_item_disable(platform, 1, True)

    # 新增一個檔案對話方塊，用於載入更多的訊息
    more = obs.obs_properties_add_path(props, 'more', '更多訊息：', obs.OBS_PATH_FILE, '文字檔案(*.txt)', None)
    # 當使用者選擇了一個檔案後，函式 load_message 將被呼叫
    obs.obs_property_set_modified_callback(more, load_message)

    # 新增一個色彩對話方塊，用於設定文字來源的色彩
    obs.obs_properties_add_color(props, 'color', '色彩：')
    # 新增一個字型對話方塊，用於設定文字來源的字型
    obs.obs_properties_add_font(props, 'font', '字型：')

    # 新增一個可編輯清單方塊，用於設定文字來源的文字
    obs.obs_properties_add_editable_list(props, 'my_texts', '文字來源文字：', obs.OBS_EDITABLE_LIST_TYPE_STRINGS, None, None)

    # 建立群組方塊對應的屬性集
    login_props = obs.obs_properties_create()
    # 新增一個群組方塊，他包含了用於登入的子控製項
    obs.obs_properties_add_group(props, 'group_login', '使用者登入', obs.OBS_GROUP_NORMAL, login_props)
    obs.obs_properties_add_text(login_props, 'username', '使用者名稱：', obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_text(login_props, 'password', '密碼：', obs.OBS_TEXT_PASSWORD)
    # 新增一個登入按鈕
    obs.obs_properties_add_button(login_props, 'login', '登入', login)

    # 新增一個按鈕，點選後將移除自己
    obs.obs_properties_add_button(props, 'remove', '移除我自己', remove_myself)

    # 新增一個按鈕，用於為訊息文字方塊選擇隨機文字
    obs.obs_properties_add_button(props, 'random_text', '隨機訊息', set_random_text)
    return props


def script_update(settings):
    # 使用者編輯控製項後，將最新的腳本設定應用至場景
    set_source_color(settings)
    set_source_font(settings)
    

def script_defaults(settings):
    # 設定控製項的預設值
    obs.obs_data_set_default_bool(settings, 'auto', True)
    obs.obs_data_set_default_double(settings, 'delay', 1.5)


# 變數 current_settings 用於表示腳本設定
current_settings = None

# 執行任務的函式 task
def task():
    obs.script_log(obs.LOG_INFO, '任務開始了')
    obs.remove_current_callback()

    # 顯示文字方塊中的訊息
    message = obs.obs_data_get_string(current_settings, 'message')
    obs.script_log(obs.LOG_INFO, f'訊息為 {message if message else "[空]"}')
    # 顯示選擇的串流平臺
    platform = obs.obs_data_get_string(current_settings, 'platform')
    obs.script_log(obs.LOG_INFO, f'串流平臺為 {platform}')

    # 隨機選擇項作為文字來源的文字
    set_source_text(current_settings)


def script_load(settings):
    global current_settings
    current_settings = settings

    # 是否在腳本載入後執行任務？
    if obs.obs_data_get_bool(settings, 'auto'):
        obs.script_log(obs.LOG_INFO, f'在啟動時執行任務（是的）')

        # 新增執行任務的計時器，時間間隔為滑桿表示的秒數
        seconds = obs.obs_data_get_double(settings, 'delay')
        obs.script_log(obs.LOG_INFO, f'請等待大約 {seconds} 秒')
        obs.timer_add(task, int(seconds * 1000))
