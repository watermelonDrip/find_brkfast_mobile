#/Users/luoman/PycharmProjects/find_brkfast_mobile/my_brkfst.py

from kivy.config import Config
import os
# 引入资源目录,如res目录位于项目根目录下，写相对路径(不要写绝对路径)相当于告诉kivy　DroidSansFallback.ttf 字体位于res目录中
fn_regular='/Users/luoman/opt/anaconda3/envs/find_brkfast_mobile/lib/python3.9/site-packages/kivy/data/fonts/msyh.ttf'
from kivy.resources import resource_add_path, resource_find
resource_add_path(os.path.abspath('fn_regular'))
# 替换kivy中的默认字体，使用我们的新字体
#from kivy.core.text import LabelBase
#LabelBase.register('Roboto', 'msyh.ttf')
import kivy


from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen

#LabelBase.register(name='Microsoft YaHei UI', fn_regular='./fonts/msyh.ttf')


#LabelBase.register(name='Microsoft YaHei UI', fn_regular='/Users/luoman/opt/anaconda3/envs/find_brkfast_mobile/lib/python3.9/site-packages/kivy/data/fonts/msyh.ttf')
class Demo(MDApp):

    def build(self):

        self.food = {'0':'粉面类','1':'饺子','2':'米饭','3':'粥','4':'饼','5':'面包','6':'杂粮'}
        self.method = {'0':'水煮（清汤）','1':'水煮（火锅汤底）','2':'水煮（呛汤）','3':'水煮（酸汤）','4':'水煮（菌汤）','5':'清蒸','6':'油煎','7':'油炸','8':'油焖','9':'炒','10':'干拌'}

        # defining screen
        screen = Screen()

        # defining lables
        tmp_food = self.food
        tmp_method = self.method

        ld = [0]*len(tmp_food)

        for i in range(len(tmp_food)):
            ld[i] = MDLabel(text= str(i+1) +"."+  tmp_food[str(i)], pos_hint={'center_x': 0.8,
                                                   'center_y': 0.8-0.05*i},
                        theme_text_color="Custom",
                        text_color=(0.5, 0, 0.5, 1),
                        font_style='Caption')


        l3 = MDLabel(text='d谁谁谁', font_name=fn_regular,pos_hint={'center_x': 0.8,
                                               'center_y': 0.8},
                    theme_text_color="Custom",
                    text_color=(0.5, 0, 0, 1),
                    font_style='Caption')

        # defining 1st label



        l = MDLabel(text="Welcome!", pos_hint={'center_x': 0.8,
                                               'center_y': 0.8},
                    theme_text_color="Custom",
                    text_color=(0.5, 0, 0.5, 1),
                    font_style='Caption')

        # defining 2nd label
        l1 = MDLabel(text=" ", pos_hint={'center_x': 0.8,
                                                'center_y': 0.8},
                     theme_text_color="Custom",
                     text_color=(0.5, 0, 0.5, 1),
                     font_style='H2')

        # defining 3rd label
        l2 = MDLabel(text="Welcome!", pos_hint={'center_x': 0.8,
                                                'center_y': 0.2},
                     theme_text_color="Custom",
                     text_color=(0.5, 0, 0.5, 1),
                     font_style='H1')
       # for i in range(len(tmp_food)):
        #    screen.add_widget(ld[i])


       # screen.add_widget(l)

       # screen.add_widget(l1)
       # screen.add_widget(l2)
        screen.add_widget(l3)

        return screen


if __name__ == "__main__":
    Demo().run()