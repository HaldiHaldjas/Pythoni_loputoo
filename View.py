from tkinter import *
import tkinter.font as font
from tkinter import messagebox, filedialog
#  from tkinter.ttk import Treeview

class View(Tk):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.__width = 500
        self.__height = 300
        self.default_font = font.Font(family='Verdana', size=14)
        # akna omadused

        self.title('Otsing faili sisust')
        self.center_window(self.__width, self.__height)

        # frame loomine
        self.top_frame = self.create_top_frame()
        self.bottom_frame = self.create_bottom_frame()

        # vidinate loomine
        (self.lbl_entry, self.search_entry, self.message, self.btn_choose_file, self.btn_search,
         self.result_box) = self.create_frame_widgets()

        # enter klahvi vajutus
        # self.bind('<Return>', self.controller.select_file)
        #  self.protocol('WM_DELETE_WINDOW', self.on_close)

    def main(self):
        self.mainloop()

    # asetab akna ekraani keskele
    def center_window(self, width, height):
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def create_top_frame(self):
        frame = Frame(self, bg='grey')
        frame.pack(expand=True, fill=BOTH)
        return frame

    def create_bottom_frame(self):
        frame = Frame(self, bg='lightgrey')
        frame.pack(expand=True, fill=BOTH)
        return frame

    def create_frame_widgets(self):
        lbl_search_entry = Entry(self.top_frame)
        lbl_search_entry.grid(row=1, column=3, padx=10, pady=10)
        lbl_search_entry.focus()

        lbl_entry = Label(self.top_frame, text='Sisesta otsingusõna', font=self.default_font)
        lbl_entry.grid(row=1, column=4, padx=5, pady=5)

        message = Label(self.top_frame, text='Veateade', foreground='red', background='lemonchiffon')
        message.grid(row=3, column=4, padx=5, pady=5)

        btn_choose_file = Button(self.top_frame, text='Vali fail', font=self.default_font, command=self.select_file)
        btn_choose_file.grid(row=2, column=4, padx=5, pady=5)

        btn_search = Button(self.top_frame, text='Otsi', font=self.default_font, command=self.search_click)
        btn_search.grid(row=3, column=4, padx=5, pady=5)

        result_box = Text(self.bottom_frame, bg='white', font=self.default_font)
        scrollbar = Scrollbar(self.bottom_frame, orient=VERTICAL)
        scrollbar.config(command=result_box.yview)
        result_box.configure(yscrollcommand = scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
        result_box.pack(expand=True, fill=BOTH, padx = 5, pady = 5)

        return lbl_entry, lbl_search_entry, message, btn_choose_file, btn_search, result_box

    def select_file(self):
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )
        filename = filedialog.askopenfilename(
            title='Ava fail',
            filetypes=filetypes)
        if filename:
            # votab kontrollerist faili nime
            self.controller.set_file_name(filename)


    def search_click(self):
        self.controller.search_button_click(self.search_entry.get())
        print(self.search_entry.get())

    def show_error(self, message):
        message['text'] = message
        message['foreground'] = 'red'
        message.after(3000, self.hide_message)

    def hide_message(self):
        self.message['text'] = ''

    def show_results(self, result):
        for line in result:
            self.result_box.insert(END, line + '\n')
            # print(line)

        # my_table = Treeview(frame)















