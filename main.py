import kivy
# kivy.require('2.3.1') # adjust the minimum required Kivy version as needed

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.properties import StringProperty

# Define the screens in Kv language for cleaner structure
Builder.load_string("""
<Menu>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Welcome to the Menu!'
            font_size: 32
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text: 'Calculator'
                on_press: root.manager.current = 'Calculator'
            Button:
                text: 'Settings'
                on_press: root.manager.current = 'Settings'
<Settings>
    BoxLayout:
        orientation: 'horizontal'
        Button:
            text: 'exit'
            on_press: root.manager.current = 'Menu'
<Calculator>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: display_label
            text: root.display_text
            font_size: 32
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text: 'C'
                on_press: root.clear_all()
            Button:
                text: 'CE'
                on_press: root.remove_char()
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text: '7'
                on_press: root.add_char(self.text)
            Button:
                text: '8'
                on_press: root.add_char(self.text)
            Button:
                text: '9'
                on_press: root.add_char(self.text)
            Button:
                text: '+'
                on_press: root.add_char(self.text)
                on_press: root.set_operator(self.text)
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text: '4'
                on_press: root.add_char(self.text)
            Button:
                text: '5'
                on_press: root.add_char(self.text)
            Button:
                text: '6'
                on_press: root.add_char(self.text)
            Button:
                text: '-'
                on_press: root.set_operator(self.text)
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text: '1'
                on_press: root.add_char(self.text)
            Button:
                text: '2'
                on_press: root.add_char(self.text)
            Button:
                text: '3'
                on_press: root.add_char(self.text)
            Button:
                text: '*'
                on_press: root.set_operator(self.text)
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text: '0'
                on_press: root.add_char(self.text)
            Button:
                text: ','
                on_press: root.add_char(self.text)
            Button:
                text: '='
                on_press: root.calculate()
            Button:
                text: '/'
                on_press: root.set_operator(self.text)
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text: 'exit'
                on_press: root.manager.current = 'Menu'
""")

class Menu(Screen):
    pass

class Settings(Screen):
    pass

class Calculator(Screen):
    display_text = StringProperty("")
    first_value = ""
    operator = ""
    
    def add_char(self, char):
        self.display_text += char

    def remove_char(self):
        if self.display_text:
            self.display_text = self.display_text[:-1]
            
    def clear_all(self):
        self.display_text = ""
        self.first_value = ""
        self.operator = ""
    
    def set_operator(self, op):
        if not self.display_text:
            return
        if self.display_text[-1] in "+-*/":
            return

        self.first_value = self.display_text
        self.operator = op
        self.display_text = ""
        
    def calculate(self):
        if self.first_value and self.operator and self.display_text:
            expression = f"{self.first_value}{self.operator}{self.display_text}"

            try:
                result = str(eval(expression))
                self.display_text = result
            except Exception:
                self.display_text = ""

            # reset post-calc
            self.first_value = ""
            self.operator = ""

class ScreenApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Menu(name='Menu'))
        sm.add_widget(Calculator(name='Calculator'))
        sm.add_widget(Settings(name='Settings'))
        return sm

if __name__ == '__main__':
    ScreenApp().run()

# tasks:
# make a menu screen
# add screen switching buttons


# from kivy.uix.popup import Popup
# from kivy.uix.label import Label
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout
# from kivy.app import App
# from kivy.core.window import Window

# class TestApp(App):
#     def build(self):
#         # Create the content for the popup
#         content = BoxLayout(orientation='vertical')
#         content.add_widget(Label(text='Hello world'))
#         close_button = Button(text='Close', size_hint_y=None, height=40)
#         content.add_widget(close_button)

#         # Create the Popup widget
#         self.popup = Popup(title='Test popup',
#                            content=content,
#                            size_hint=(None, None), size=(400, 400),
#                            auto_dismiss=False)

#         # Bind the close button press to the popup's dismiss method
#         close_button.bind(on_release=self.popup.dismiss)

#         # Main window content button to open the popup
#         open_button = Button(text='Open Popup')
#         open_button.bind(on_release=self.popup.open)
#         return open_button

# if __name__ == '__main__':
#     TestApp().run()
