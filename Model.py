import csv
from tkinter import filedialog, messagebox


class Model:
    def __init__(self):
        self.__data = None


    def select_file(self):
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )
        filename = filedialog.askopenfilename(
            title='Ava fail',
            initialdir='/',
            filetypes=filetypes)
        if filename:
            self.process_file(filename)

    def process_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.data = file.read()

        except FileNotFoundError:
            messagebox.showerror('Viga, faili ei õnnestunud leida!')

    def search_data(self):
        if self.data is None:
            messagebox.showerror('Viga, faili ei saanud avada!')
            search = self.view.lbl_entry.get()
            if not search:
                messagebox.showerror('Viga, otsitut ei leitud!')
                return

            search_results = []
            for row in self.data:
                for item in row:
                    if search in item:
                        search_results.append(row)
                        break

            if search_results:
                self.view.result_box('Otsingu tulemused: ', search_results)
            else:
                self.view.result_box('Ei leitud')

