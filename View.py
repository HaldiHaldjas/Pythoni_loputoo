from email import header
from tkinter import *
import tkinter.font as font
from tkinter import filedialog, ttk
import uuid
from tkinter.ttk import Treeview


class View(Tk):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.__width = 700
        self.__height = 500
        self.default_font = font.Font(family='Verdana', size=14)
        # akna omadused

        self.title('Otsing faili sisust')
        self.center_window(self.__width, self.__height)

        # frame loomine
        self.top_frame = self.create_top_frame()
        self.bottom_frame = self.create_bottom_frame()

        # tabeli loomine
        self.table = ttk.Treeview(self.bottom_frame)
        self.table.pack(expand=True, fill=BOTH)

        # vidinate loomine
        (self.lbl_entry, self.search_entry, self.message, self.btn_choose_file, self.btn_search) = self.create_frame_widgets()

        # self.table

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

        # result_box = Text(self.bottom_frame, fg='black', bg='white', font=self.default_font)

        # table = ttk.Treeview(self.bottom_frame)
        # table.pack(expand=True, fill=BOTH)

        return lbl_entry, lbl_search_entry, message, btn_choose_file, btn_search

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
        # print(self.search_entry.get())

    def show_error(self, message):
        message['text'] = message
        message['foreground'] = 'red'
        message.after(3000, self.hide_message)

    def hide_message(self):
        self.message['text'] = ''

    def show_results(self, header, result):
        if len(result) > 0:
            # Clear existing data in the result_box
            result_box = ttk.Treeview(self.bottom_frame)
            scrollbar = ttk.Scrollbar(self.bottom_frame, orient=VERTICAL, command=result_box.yview)
            scrollbar.pack(side=RIGHT, fill=Y)
            result_box.configure(yscrollcommand=scrollbar.set)
            result_box.heading('#0', text="Päis", anchor=W)

            column_ids = [h.lower() for h in header]
            result_box['columns'] = column_ids
            for h in header:
                result_box.heading(f'{h.lower()}', text=h, anchor=CENTER)
                result_box.column(f'{h.lower()}', anchor=CENTER, width=50)

            x = 1
            for d in result:
                result_box.insert(parent='', index=END, iid=str(x), text=str(x), values=d)
                x += 1

            result_box.pack(expand=True, fill=BOTH)


            # Create column headings if they don't exist
            if not self.result_box["columns"]:
                column_ids = [h.lower() for h in header]
                self.result_box['columns'] = column_ids
                for h in header:
                    self.result_box.heading(f'{h.lower()}', text=h, anchor=CENTER)
                    self.result_box.column(f'{h.lower()}', anchor=CENTER, width=50)

            # Insert data into the result_box
            for idx, d in enumerate(result):
                self.result_box.insert(
                    parent='',
                    index=END,
                    iid=str(idx),
                    text='',
                    values=d
                )

            # def show_results(self, header, result):
    #     if len(result) > 0:
    #         self.result_box.delete(*self.result_box.get_children())
    #         result_box = ttk.Treeview(self.bottom_frame)
    #         vsb = ttk.Scrollbar(self.bottom_frame, orient=VERTICAL, command=result_box.yview)
    #         vsb.pack(side=RIGHT, fill=Y)
    #         result_box.configure(yscrollcommand=vsb.set)
    #         result_box.column('#0', width=100, stretch=NO)
    #         result_box['columns'] = header
    #         for h in header:
    #             result_box.heading(f'{h}', text=h, anchor=CENTER)
    #             result_box.column(f'{h}', anchor=CENTER, width=50)
    #
    #         x = 0
    #         for r in result:
    #             result_box.insert(
    #                 parent='',
    #                 index=END,
    #                 iid=str(r),
    #                 text='',
    #                 values=r
    #             )
    #         r += 1

            # Insert data into the table
            # for idx, d in enumerate(result):
            #     self.result_box.insert(
            #         parent='',
            #         index=END,
            #         iid=str(idx),
            #         text='',
            #         values=d
            #     )

    # def show_results(self, header, data):
    #     # Clear existing data in the table
    #     self.table.delete(*self.table.get_children())
    #
    #     # Create column headers if they don't exist
    #     if not self.table["columns"]:
    #         column_ids = [h.lower() for h in header]
    #         self.table['columns'] = column_ids
    #         for h in header:
    #             self.table.heading(f'{h.lower()}', text=h, anchor=CENTER)
    #             self.table.column(f'{h.lower()}', anchor=CENTER, width=50)



    # def show_results(self, result):
    #     for line in result:
    #         self.result_box.insert(END, line + '\n')
    #         # print(line)

    # def show_results(self, header, data):
    #     # puhastab eelmisest infost
    #     # self.result_box.delete(1.0, END)
    #     #
    #     # if not hasattr(self, 'table'):
    #     #     self.table["columns"] = header
    #     #     self.table.heading('#0', text='Result', anchor=NW)
    #     #     self.table.column('#0', anchor=CENTER, width=2)
    #     #     for h in header:
    #     #         self.table.heading(f'{h}', text=h, anchor=CENTER)
    #     #         self.table.column(f'{h}', anchor=CENTER, width=50)
    #     #
    #     # # Lisab andmed tabelisse
    #     # for idx, line in enumerate(result):
    #     #     # annab unikaalse id
    #     #     unique_id = str(uuid.uuid4())
    #     #     self.table.insert(parent='', index=END, iid=unique_id, text='', values=line)
    #     # print(self.table)
    #
    #     # table.heading('#0', text='Result', anchor=NW)
    #     # table.column('#0', anchor=CENTER, width=2)
    #     # column_ids = self.controller.send_search_button_click()
    #     # table['columns'] = column_ids
    #     # for h in header:
    #     #     table.heading(f'{h}', text=h, anchor=CENTER)
    #     #     table.column(f'{h}', anchor=CENTER ,width=50)
    #     # x = 0
    #     # for line in result:
    #     #     table.insert(
    #     #         parent='',
    #     #         index=END,
    #     #         iid=str(x),
    #     #         text='',
    #     #         values=line
    #     #     )
    #     #     x += 1
    #     # table.pack(expand=True, fill=BOTH)
    #     # my_table = Treeview(frame)
    #     self.table.delete(*self.table.get_children())
    #     if len(data) > 0:
    #         table = ttk.Treeview(self.bottom_frame)
    #         # vsb = ttk.Scrollbar(self.__frame_bottom, orient=VERTICAL, command=table.yview)
    #         # vsb.pack(side=RIGHT, fill=Y)
    #         # table.configure(yscrollcommand=vsb.set)
    #         table.heading('#0', text='jutt', anchor=CENTER)
    #         table.column('#0', anchor=CENTER, width=2)
    #         # print(table.heading)
    #         print(table.heading('#0')['text'])
    #         column_ids = [h.lower() for h in header]
    #         table['columns'] = column_ids
    #         for h in header:
    #             table.heading(f'{h.lower()}', text=h, anchor=CENTER)
    #             table.column(f'{h.lower()}', anchor=CENTER, width=50)
    #
    #         x = 0
    #         for d in data:
    #             table.insert(
    #                 parent='',
    #                 index=END,
    #                 iid=str(x),
    #                 text='',
    #                 values=d
    #             )
    #             x += 1
    #         table.pack(expand=True, fill=BOTH)
