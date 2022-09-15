#!/usr/bin/env python3

import rospy
from kivymd.app import MDApp  ## 거의 모든 위젯(kivyMD) 사용가능
from kivy.lang import Builder
from webview import Webview
import os

""" MDApp class로 상속 받는 클래스를 만들어서 사용하면 된다 """
class TutorialApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        home = os.path.expanduser('~') + '/catkin_ws/src'  ## home/userid
        ## ros_gui.kv 파일을 불러오게 됨
        print(home)
        self.screen = Builder.load_file("{}/kivymd_ros_tutorial/ros_gui_webbrowser.kv".format(home))

    def build(self):
        return self.screen        


if __name__ == '__main__':
    rospy.init_node('simple_gui', anonymous=True)
    TutorialApp().run()