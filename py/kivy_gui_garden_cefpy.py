#!/usr/bin/env python3

import rospy
import os
from kivymd.app import MDApp  ## 거의 모든 위젯(kivyMD) 사용가능
from kivy.lang import Builder
# from kivy.garden.cefpython import CEFBrowser
# from cefpython3 import cefpython as cef


""" MDApp class로 상속 받는 클래스를 만들어서 사용하면 된다 """
class TutorialApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        home = os.path.expanduser('~') + '/catkin_ws/src'  ## home/userid
        self.screen = Builder.load_file("{}/kivymd_ros_tutorial/ros_gui_kiyv_garden_cefpython.kv".format(home))

        ## cefpython3 사용할 경우 하지만 이것도 파이썬 3.8은 안됨 # Exception: Python version not supported: 3.8.10
        # cef.Initialize()
        # cef.CreateBrowserSync(url="https://google.com")

    def build(self):
        return self.screen        


if __name__ == '__main__':
    rospy.init_node('simple_gui', anonymous=True)
    TutorialApp().run()