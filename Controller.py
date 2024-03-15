from tkinter import filedialog, messagebox

from Model import Model
from View import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def send_search_button_click(self):
        self.view.btn_search['state'] = 'normal'

    def search_button_click(self, phrase):
        self.model.set_phrase(phrase)
        self.model.compare_data()
        self.view.show_results(self.model.get_result())
        # self.view.btn_choose_file['state'] = 'normal'

    def set_file_name(self, filename):
        self.model.set_filename(filename)


    # def check(self):
    #     try:
    #         search_data = self.view.lbl_entry.get()
    #         self.view.generate_search_results()
    #     except ValueError as error:
    #         self.view.show_error(error)





