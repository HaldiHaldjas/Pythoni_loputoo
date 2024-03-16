
class Model:
    def __init__(self):
        self.__header = []
        self.__filename = None
        self.__phrase = ""
        self.__data = []
        self.__result = []

    def set_filename(self, filename):
        self.__filename = filename
        self.read_data()

    def set_phrase(self, phrase):
        self.__phrase = phrase

    def get_result(self):
        return self.__result

    def get_header(self):
        return self.__header

    # def read_data(self):
        # with open(self.__filename, 'r', encoding='utf-8') as file:
        #     self.__header = file.readlines()[0]
        #     file_context = file.readlines()[1:]
        #     for line in file_context:
        #         self.__data.append(line.strip())

    def read_data(self):
        with open(self.__filename, 'r', encoding='utf-8') as file:
            file_content = file.readlines()
            self.__header = file_content[0].strip().split(';')  # Store header without newline, split by ;
            file_context = file_content[1:]  # Exclude the header
            for line in file_context:
                self.__data.append(line.strip())
            print(self.__header)
            return self.__header, self.__data

    def compare_data(self):
        if len(self.__phrase) > 2:
            for item in self.__data:
                if self.__phrase in item:
                    print(item)
                    components = item.split(';')
                    self.__result.append(components)
        return self.__result


    # def compare_data(self, data):
    #     search_results = []
    #     for row in data:
    #         for item in row:
    #             if search in item:
    #                 search_results.append(row)
    #                 break
    #
    #     if search_results:
    #         self.__result('Otsingu tulemused: ', search)
    #     else:
    #         self.__result('Ei leitud')
    #

    # def process_file(self, filename):

    #
    #     except FileNotFoundError:
    #         messagebox.showerror('Viga, faili ei õnnestunud leida!')
    #
    # def search_data(self, data):
    #     if data is None:
    #         messagebox.showerror('Viga, faili ei saanud avada!')
    #         search = self.lbl_entry
    #         if not search:
    #             messagebox.showerror('Viga, otsitut ei leitud!')
    #             return