from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.button import Button
from kivy.properties import ListProperty

import db

import glob
import sqlite3

db_path = "./paper.db"

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
    result_list = ListProperty(['Unknown', 'None', 'Unknown', 'None'])

    def __init__(self, **kwargs):
        super(PaperInfo, self).__init__(**kwargs)
        self.f_name = "temp"

    def load_data(self, f_name):
        self.result_list = db.load_curr_info(db_path, f_name)
        self.f_name = f_name
        #self.result_list = ['Unknown', '{0}'.format(random.randint(1, 100)), 'Unknown', 'None']

    def enterInfo(self):
        db.update_info(db_path, self.f_name,
                        self.ids['Q1'].text,
                        self.ids['Q2'].text,
                        self.ids['Q3'].text,
                        self.ids['Q4'].text)


class PaperSurveyRoot(BoxLayout):
    def __init__(self, **kwargs):
        super(PaperSurveyRoot, self).__init__(**kwargs)


class PaperSurveyApp(App):

    def __init__(self, **kwargs):
        super(PaperSurveyApp, self).__init__(**kwargs)

        self.title = 'Paper Survey'
    pass


def init_db():

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS papers(name TEXT PRIMARY KEY, Q1 TEXT, Q2 TEXT, Q3 TEXT, Q4 TEXT);")
    conn.commit()
    conn.close()
if __name__=="__main__":

    init_db()
    PaperSurveyApp().run()