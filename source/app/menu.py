from app.executables import Executables


class Menu():

    __run: bool
    __executables: Executables

    def __init__(self):
        self.__run = True
        self.__executables = Executables()

    def start(self) -> None:
        self.__author_details()
        while (self.__run):
            self.__show_options() 
            option_selected = self.__read_option()
            self.__run = False if option_selected == 3 else True
            self.__execute_option(option_selected)


    def __author_details(self) -> None:
        print("""
        |-----------------------------------------|
        | Name: Cesar Javier Sanchez Hernandez    |
        | Group: 9 - A                            |
        |-----------------------------------------|""")

    def __show_options(self) -> None:
        print("""
                ------ Options ------""")
        print("""
        1.- Run automated charts exercise
        2.- Run automated sign up exercise
        3.- Exit""")

    def __read_option(self) -> int:
        try:
            option_selected = int(input("""
        Enter your option: """))
        except ValueError:
            print("""
            xxxxx Invalid option selected xxxxx
            """)
            option_selected = 3
        return option_selected

    def __execute_option(self, option_selected: int) -> None:
        if option_selected == 1:
            self.__executables.menu_automated_charts()
        elif option_selected == 2:
            self.__executables.menu_automated_sign_up()
        elif option_selected == 3:
            print("""
                    ooooo Exit ooooo
            """)
            exit()
        else:
            print("""
            xxxxx That option dosen't exist xxxxx
            """)
            exit()
    
    