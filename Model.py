from tkinter import filedialog, messagebox


class Model:
    def __init__(self):
        self.__lbl_entry = None
        self.__data = None



    def compare_data(self, data):
            search_results = []
            for row in data:
                for item in row:
                    if search in item:
                        search_results.append(row)
                        break

            if search_results:
                self.view.result_box('Otsingu tulemused: ', search_results)
            else:
                self.view.result_box('Ei leitud')

