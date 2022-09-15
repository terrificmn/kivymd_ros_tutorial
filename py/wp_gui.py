#!/usr/bin/env python3

import rospy
from std_msgs.msg import Empty
from kivymd.app import MDApp  #  거의 모든 위젯(kivyMD) 사용가능
from kivy.lang import Builder
import os

# """ MDApp class로 상속 받는 클래스를 만들어서 사용하면 된다 """
class WpApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        home = os.path.expanduser('~') + '/catkin_ws/src'  ## home/userid
        ## ros_gui.kv 파일을 불러오게 됨
        print(home)
        self.screen = Builder.load_file("{}/kivymd_ros_tutorial/ros_gui_wp.kv".format(home))

    def build(self):
        return self.screen        

    def saveWp(self, *args):
        print("published")
        
        self.screen.ids.center_label.text = 'save one waypoint' # kv파일에 정의한 위젯의 id에 해당하는 txt를 바꿈
        msg = Empty()
        save_pub.publish(msg)

    def loadWp(self, *args):
        print("published.. to load..")
        msg = Empty()
        load_pub.publish(msg)
        self.screen.ids.center_label.text = 'start...'

    def resetWp(self, *args):
        print("published.. to reset..")
        msg = Empty()
        reset_pub.publish(msg)
        self.screen.ids.center_label.text = 'reset...'


if __name__ == '__main__':
    rospy.init_node('waypoint_gui', anonymous=True)
    reset_pub = rospy.Publisher('/reset_path', Empty, queue_size=1)
    save_pub = rospy.Publisher('/save_path', Empty, queue_size=1)
    load_pub = rospy.Publisher('/read_start', Empty, queue_size=1)
    
    WpApp().run()