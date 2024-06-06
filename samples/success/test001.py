# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

import win32api

auto_setup(__file__)

touch(Template(r"tpl1685950531338.png", record_pos=(-0.002, 0.036), resolution=(1296, 759)))

# get current window
current_window = device()

# for 20 to clear account input text 
for i in range(20):
    current_window.keyboard.SendKeys("{VK_BACK}")

text("Geekmister")
touch(Template(r"tpl1685953737569.png", record_pos=(0.002, 0.073), resolution=(1296, 759)))

# for 20 to clear account input text 
for i in range(20):
    current_window.keyboard.SendKeys("{VK_BACK}")
    
text("abc123...")
touch(Template(r"tpl1685953779009.png", record_pos=(0.0, 0.13), resolution=(1296, 759)))
sleep(5)


touch(Template(r"tpl1685953931465.png", record_pos=(-0.343, -0.008), resolution=(1296, 759)))

touch(Template(r"tpl1685953950213.png", record_pos=(0.336, -0.142), resolution=(1296, 759)))

text("元宇宙")
touch(Template(r"tpl1685954029025.png", record_pos=(-0.336, -0.034), resolution=(1296, 759)))
assert_exists(Template(r"tpl1685954048401.png", record_pos=(-0.346, -0.033), resolution=(1296, 759)), "课程主题展示在左侧")


    

