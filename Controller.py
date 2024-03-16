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
        result = self.model.get_result()
        header = self.model.get_header()  # Assuming you have a method to retrieve the header
        self.view.show_results(header, result)

    # def search_button_click(self, phrase):
    #     self.model.set_phrase(phrase)
    #     self.model.compare_data()
    #     self.view.show_results(self.model.get_result())
        # testin headerit
        # self.model.read_data()
        # result, header = self.model.read_data()
        # header = self.model.get_header()
        # if header is not None:
        #     self.view.show_results(results, header)
        # # self.view.btn_choose_file['state'] = 'normal'
        # else:
        #     self.view.show_error('Ei leia päist!')

    def set_file_name(self, filename):
        self.model.set_filename(filename)






