import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
import kivy
# kivy.require('2.3.1') # adjust the minimum required Kivy version as needed

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty, NumericProperty

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
                text: 'Dictionary'
                on_press: root.manager.current = 'Dictionary'
            Button:
                text: 'Settings'
                on_press: root.manager.current = 'Settings'
                    
<Settings>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Settings'
            font_size: 32
        Button:
            text: 'exit'
            on_press: root.manager.current = 'Menu'

<Dictionary>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Welcome to the Dictionary!'
            font_size: 32
        Button:
            text: 'Quintessential'
            on_press: root.manager.current = 'Quintessential'
        Button:
            text: 'Dictionary (programming)'
            on_press: root.manager.current = 'Dictionary_definition'
        Button:
            text: 'Questionnaire'
            on_press: root.manager.current = 'Questionnaire'
        Button:
            text: 'exit'
            on_press: root.manager.current = 'Menu'

<Questionnaire>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Questionnaire'
            size_hint_y: 0.2
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: root.question
            GridLayout:
                cols: 2
                rows: 2
                Button:
                    text: root.options[0]
                    id: opt0
                    on_release: root.check_ans(self.text)
                Button:
                    text: root.options[1]
                    id: opt1
                    on_release: root.check_ans(self.text)
                Button:
                    text: root.options[2]
                    id: opt2
                    on_release: root.check_ans(self.text)
                Button:
                    text: root.options[3]
                    id: opt3
                    on_release: root.check_ans(self.text)
        Button:
            text: 'Back to Dictionary'
            size_hint_y: 0.2
            on_press: root.manager.current = 'Dictionary'
            
<Quintessential>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Quintessential means representing the most perfect or typical example of a quality or class.'
            
        Button:
            text: 'exit'
            on_press: root.manager.current = 'Dictionary'
                    
<Dictionary_programming>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'A dictionary is a collection of key-value pairs.'
            font_size: 24
        Button:
            text: 'exit'
            on_press: root.manager.current = 'Dictionary'
                    
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

class Dictionary(Screen):
    pass

class Quintessential(Screen):
    pass

class Dictionary_programming(Screen):
    pass

class Questionnaire(Screen):
    question = StringProperty("Loading...")
    options = ListProperty(["", "", "", ""])
    result = StringProperty("")
    score = NumericProperty(0)
    answer_key = NumericProperty(0)
    # question_list = {
    #     "What is the meaning of 'Quintessential'?":["being most perfect/typical example of sth", "absolutely necessary", 
    #                                                 "not genuine", "a person's knowledge/experience of sth"],
    #     "What is the meaning of 'Dictionary' in programming?":["a data structure that holds a collection of data as a set of key-value pairs",
    #                                                            "a data structure that holds a collection of data items or elements in a sequence",
    #                                                            "symbolic names that refer to objects (values) stored in memory",
    #                                                            "a reference work on a particular subject, the items of which are typically arranged in alphabetical order"]
    #     }
    question_list = [
    {
        "question": "What is the meaning of 'Quintessential'?",
        "options": [
            "being most perfect/typical example of sth",
            "absolutely necessary",
            "not genuine",
            "a person's knowledge/experience of sth"
        ],
        "correct": 0
    },
    {
        "question": "What is the meaning of 'Dictionary' in programming?",
        "options": [
            "a data structure that holds a collection of data as a set of key-value pairs",
            "a data structure that holds a collection of data items or elements in a sequence",
            "symbolic names that refer to objects (values) stored in memory",
            "a reference work on a particular subject, the items of which are typically arranged in alphabetical order"
        ],
        "correct": 0
    }
]
    question_list = question_list

    def load_question(self):
        q = self.questions[self.current_index]
        self.question = q["question"]
        self.options = q["options"]
        self.answer_key = q["correct"]

        # reset buttons
        for btn in self.ids.values():
            btn.background_color = (1, 1, 1, 1)
            btn.disabled = False

    def on_enter(self):
        self.score = 0
        self.answer_key = 0

        q = self.question_list[self.answer_key]

        self.question = q["question"]
        self.options = q["options"]
        self.answer_key = q["correct"]

        # reset buttons
        for btn in self.ids.values():
            btn.background_color = (1, 1, 1, 1)
            btn.disabled = False

    # def on_enter(self):
    #     self.score = 0
    #     q_key = list(self.question_list.keys())[0]
    #     self.question = q_key
    #     self.options = self.question_list[q_key]
    #     self.answer_key = 0

    def check_ans(self, choice_index):
        correct_btn = self.ids[f"opt{self.answer_key}"]
        chosen_btn = self.ids[f"opt{choice_index}"]
        # user_pick = self.options.index(choice)
        self.result = ""
        if choice_index == self.answer_key:
            correct_btn.background_color = (0, 1, 0, 1)
            self.score += 1
            popup.open()
        else:
            chosen_btn.background_color = (1, 0, 0, 1)
        for btn in self.ids.values():
            btn.disabled = True
        # if user_pick == self.answer_key:
        #     self.result = "Correct!"
        #     if self.score >= 1:
        #         self.score += 0
        #     elif self.score == 0:
        #         self.score += 1
        # else:
        #     self.result = "Incorrect!"
        popup = Popup(title='Result',
                          content=Label(text=f'Your score is: {self.score}'),
                          size_hint=(None, None), size=(400, 200))

class QuintessentialQuestionnaire(Screen):
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
        sm.add_widget(Dictionary(name='Dictionary'))
        sm.add_widget(Quintessential(name='Quintessential'))
        sm.add_widget(Dictionary_programming(name='Dictionary_definition'))
        sm.add_widget(Settings(name='Settings'))
        sm.add_widget(Questionnaire(name='Questionnaire'))
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
