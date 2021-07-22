import kivy

from kivy.app import App
from kivy.uix.label import Label

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

root = Builder.load_string('''
Screen:
    BoxLayout:
        orientation:'vertical'
        Label:
            text: "1"
            font_size: self.height*0.1
            size_hint: (0.1, 0.1)
         

    Label:
        text: '欢迎来到早餐屋子！ 选一下早餐吧！'
       
''')

class MyApp(App):
    def build(self):
        root.size_hint = (1.0, 1.0)
        return root

if __name__ == '__main__':
    MyApp().run()