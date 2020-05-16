from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.button import Button

import glob

class MyButton(Button):
    def print_data(self, data):
        print(data)

class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': x} for x in sorted(glob.glob("./papers/*.pdf"))]


class PaperListForm(BoxLayout):
    def __init__(self, **kwargs):
        super(PaperListForm, self).__init__(**kwargs)


class PaperInfo(BoxLayout):
    def __init__(self, **kwargs):
        super(PaperInfo, self).__init__(**kwargs)
        self.Q1_result = 'Unknown'
        self.Q2_result = "None"
        self.Q3_result = 'Unknown'
        self.Q4_result = "None"


    def enterInfo(self):
        print(self.ids['Q1'].text)
        print(self.ids['Q2'].text)
        print(self.ids['Q3'].text)
        print(self.ids['Q4'].text)


class PaperSurveyRoot(BoxLayout):
    def __init__(self, **kwargs):
        super(PaperSurveyRoot, self).__init__(**kwargs)


class PaperSurveyApp(App):

    def __init__(self, **kwargs):
        super(PaperSurveyApp, self).__init__(**kwargs)

        self.title = 'Paper Survey'
    pass


if __name__=="__main__":
    PaperSurveyApp().run()