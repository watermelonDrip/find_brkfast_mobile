# 导入kivy库
import kivy
# 要求的版本即当前版本
kivy.require("1.11.1")

# 我们所创建的App类要继承的父类
from kivy.app import App
# 我们所创建的App要用到的Label部件
from kivy.uix.label import Label

# 定义一个App类
class TestApp(App):
    def build(self):
        # 显示标签的文本
        return Label(text ="这是一个标傻逼沙发所发生的签")

# 创建对象
label = TestApp()
# 运行窗口
label.run()
