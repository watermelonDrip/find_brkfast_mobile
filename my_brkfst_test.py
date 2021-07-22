# 导入kivy库
import kivy
# 要求的版本即当前版本
#kivy.require("1.11.1")

# 我们所创建的App类要继承的父类
from kivy.app import App
# 我们所创建的App要用到的Label部件
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button

from kivy.lang import Builder

from kivy.uix.screenmanager import ScreenManager, Screen
#Builder.load_string("""
#<MenuScreen>:
#    BoxLayout:
 #       Button:
  #          text: 'Goto settings'
  #          on_press: root.manager.current = 'settings'
  #      Button:
    #        text: 'Quit'

#<SettingsScreen>:
 #   BoxLayout:
   #     Button:
    #        text: 'My settings button'
   #     Button:
    #        text: 'Back to menu'
    #        on_press: root.manager.current = 'menu'
#""")
#class MenuScreen(Screen):
#    pass

#class SettingsScreen(Screen):
 #   pass
class MyLabel(Label):
    def on_size(self, *args):
        self.text_size = self.size


class TestApp(App):

    def build(self):
        self.foreground_color = (1, 0, 0, 1)

        food = {'0':'粉面类','1':'饺子','2':'米饭','3':'粥','4':'饼','5':'面包','6':'杂粮'}
        method = {'0':'水煮（清汤）','1':'水煮（火锅汤底）','2':'水煮（呛汤）','3':'水煮（酸汤）','4':'水煮（菌汤）','5':'清蒸','6':'油煎','7':'油炸','8':'油焖','9':'炒','10':'干拌'}
        # defining screen
        screen = Screen()

        head_line1 = Label(text="Welcome to my Home!.\nPlease enter your decision for Dr.Zhao and the wife's breakfast. ",
                           pos_hint={'center_x': 0.5,
                                     'center_y': 0.75 }, color=[0, 0, 0, 1])

        #wx.StaticText(self.panel, -1, "Please choose one  :", pos=(10 + 40, 220))


        lf = [0]*len(food)

        for i in range(len(food)):
            temp = len(food[str(i)])
            lf[i] = Label(text= str(i+1) +"."+  food[str(i)], pos_hint={'center_x': 0.2+temp*0.02,
                                                   'center_y': 0.65-0.05*i}, halign="left",color=[0, 0, 0, 1])

        lm = [0]*len(method)
        for i in range(len(method)):
            temp = len(method[str(i)])
            lm[i] = Label(text= str(i+1) +"."+  method[str(i)], pos_hint={'center_x': 0.7+temp*0.01,
                                                   'center_y': 0.65-0.05*i}, halign="left",color=[0, 0, 0, 1])
        l = Label(text="Welcome!", pos_hint={'center_x': 0.8,
                                               'center_y': 1},)

        image = Image(source="./data/images/WechatIMG342.jpeg", allow_stretch=True, keep_ratio=False)

        screen.add_widget(image)
        screen.add_widget(head_line1)
       # screen.add_widget(l)
        for i in range(len(food)):
            screen.add_widget(lf[i])


        for j in range(len(method)):
            screen.add_widget(lm[j])

        mybutton = Button(text="傻逼", size_hint=(0.2,.20), font_size=40)
        #btn.bind(on_press=callback)
        #screen.add_widget(mybutton)

        def callback(instance):
            print('The button <%s> is being pressed' % instance.text)

        btn1 = Button(text='Hello world 1')
        btn1.bind(on_press=callback)


        def callback(instance, value):
            print('My button <%s> state is <%s>' % (instance, value))

        btn1 = Button(text='选一个小婊砸！')
        btn1.bind(state=callback)

        button = Button(text=' 选一个小婊砸', size_hint=(.2, .1),
                        pos_hint={'x': .3, 'y': .2})
        screen.add_widget(button)

        return screen


if __name__ == '__main__':
    TestApp().run()