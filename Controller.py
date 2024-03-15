from tkinter import filedialog, messagebox

from Model import Model
from View import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def send_search_button_click(self):
        self.view.btn_search['state'] = 'normal'

    def search_button_click(self):
        self.view.btn_choose_file['state'] = 'normal'

    def check(self, search_input):
        try:
            input = Model(self, self.__data, self.__lbl_entry)
            self.view.generate_search_results({})





