#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int8
from kivymd.app import MDApp  ## 거의 모든 위젯(kivyMD) 사용가능
from kivy.lang import Builder

""" MDApp class로 상속 받는 클래스를 만들어서 사용하면 된다 """
class TutorialApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        ## ros_gui.kv 파일을 불러오게 됨
        self.screen = Builder.load_file('/home/sgtubunamr/catkin_ws/src/py_kivy_tutorial/ros_gui.kv')

    def build(self):
        return self.screen        

    def sliderFunction(self, slider_value):
        print(int(slider_value))

        msg = int(slider_value)
        slider_pub.publish(msg)

if __name__ == '__main__':

    slider_pub = rospy.Publisher('slider', Int8, queue_size=1)

    rospy.init_node('simple_gui', anonymous=True)
    TutorialApp().run()