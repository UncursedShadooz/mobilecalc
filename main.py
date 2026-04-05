import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty, NumericProperty

Builder.load_string("""

<Menu>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Welcome to the Menu!'
            font_size: 32
        BoxLayout:
            Button:
                text: 'Calculator'
                on_press: root.manager.current = 'Calculator'
            Button:
                text: 'Quiz'
                on_press: root.manager.current = 'Quiz'
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
            text: 'Exit'
            on_press: root.manager.current = 'Menu'

<Quiz>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Welcome to the Quiz!'
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
            text: 'Exit'
            on_press: root.manager.current = 'Menu'

<Quintessential>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Quintessential means representing the most perfect or typical example of a quality or class.'
        Button:
            text: 'Back'
            on_press: root.manager.current = 'Quiz'

<Quiz_programming>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'A Quiz is a collection of key-value pairs.'
            font_size: 24
        Button:
            text: 'Back'
            on_press: root.manager.current = 'Quiz'

<Questionnaire>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: root.question
            size_hint_y: 0.3

        GridLayout:
            cols: 2
            rows: 2

            Button:
                id: opt0
                text: root.options[0]
                on_release: root.check_ans(0)

            Button:
                id: opt1
                text: root.options[1]
                on_release: root.check_ans(1)

            Button:
                id: opt2
                text: root.options[2]
                on_release: root.check_ans(2)

            Button:
                id: opt3
                text: root.options[3]
                on_release: root.check_ans(3)

        Button:
            text: 'Back to Quiz'
            size_hint_y: 0.2
            on_press: root.manager.current = 'Quiz'

<Calculator>:
    BoxLayout:
        orientation: 'vertical'

        Label:
            text: root.display_text
            font_size: 32

        BoxLayout:
            Button:
                text: 'C'
                on_press: root.clear_all()
            Button:
                text: 'CE'
                on_press: root.remove_char()

        BoxLayout:
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
                on_press: root.set_operator(self.text)

        BoxLayout:
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
            Button:
                text: '0'
                on_press: root.add_char(self.text)
            Button:
                text: '.'
                on_press: root.add_char(self.text)
            Button:
                text: '='
                on_press: root.calculate()
            Button:
                text: '/'
                on_press: root.set_operator(self.text)

        Button:
            text: 'Back to Menu'
            on_press: root.manager.current = 'Menu'
""")

class Menu(Screen):
    pass

class Settings(Screen):
    pass

class Quiz(Screen):
    pass

class Quintessential(Screen):
    pass

class Quiz_programming(Screen):
    pass


class Questionnaire(Screen):

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
            "question": "What is the meaning of 'Quiz' in programming?",
            "options": [
                "a data structure that holds a collection of data as a set of key-value pairs",
                "a sequence of values",
                "a variable reference",
                "a book of words"
            ],
            "correct": 0
        },
        {
            "question": "What is 58 x 49?",
            "options": [
                "3261",
                "2482",
                "3216",
                "2842"
            ],
            "correct": 3
        }
    ]

    question = StringProperty("")
    options = ListProperty(["", "", "", ""])
    score = NumericProperty(0)

    question_index = NumericProperty(0)
    correct_answer = NumericProperty(0)

    def on_enter(self):

        self.score = 0
        self.question_index = 0

        q = self.question_list[self.question_index]

        self.question = q["question"]
        self.options = q["options"]
        self.correct_answer = q["correct"]

        for btn in self.ids.values():
            btn.background_color = (1,1,1,1)
            btn.disabled = False

    def check_ans(self, choice_index):

        correct_btn = self.ids[f"opt{self.correct_answer}"]
        chosen_btn = self.ids[f"opt{choice_index}"]

        if choice_index == self.correct_answer:
            correct_btn.background_color = (0,1,0,1)
            self.score += 1
        else:
            chosen_btn.background_color = (1,0,0,1)
            correct_btn.background_color = (0,1,0,1)

        for btn in self.ids.values():
            btn.disabled = True

        popup = Popup(
            title="Result",
            content=Label(text=f"Score: {self.score}"),
            size_hint=(None,None),
            size=(400,200)
        )
        popup.open()


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
            except:
                self.display_text = ""

            self.first_value = ""
            self.operator = ""


class ScreenApp(App):

    def build(self):

        sm = ScreenManager()

        sm.add_widget(Menu(name='Menu'))
        sm.add_widget(Calculator(name='Calculator'))
        sm.add_widget(Quiz(name='Quiz'))
        sm.add_widget(Quintessential(name='Quintessential'))
        sm.add_widget(Quiz_programming(name='Dictionary_definition'))
        sm.add_widget(Settings(name='Settings'))
        sm.add_widget(Questionnaire(name='Questionnaire'))

        return sm


if __name__ == '__main__':
    ScreenApp().run()