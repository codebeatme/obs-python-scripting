# WARNING 该文件为测试文件，并不会产生预期效果
# 导入模块 obspython
from typing import Any
import obspython as obs

import ctypes

class media_frames_per_second(ctypes.Structure):
      
    def __init__(self, *args: Any, **kw: Any) -> None:
        super().__init__(*args, **kw)
        self.numerator = 0
        self.denominator = 0

def script_properties():
    props = obs.obs_properties_create()

    # 添加一个按钮
    prop = obs.obs_properties_add_frame_rate(props, 'output', '输出')

    obs.obs_property_frame_rate_option_add(prop, 'high', '高')
    obs.obs_property_frame_rate_fps_range_add(prop, media_frames_per_second(), media_frames_per_second())
    return props
