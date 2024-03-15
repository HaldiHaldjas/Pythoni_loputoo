from Controller import Controller
# from Model import Model
# from View import View

class App:
    def __init__(self): #  konstruktor, mis käivitatakse iga kord
        app = Controller()
        app.view.main()  #  Teeb põhiakna nähtavaks

if __name__ == "__main__":  #  käivitab selle faili
    App()