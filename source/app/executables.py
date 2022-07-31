import json
from app.automated_charts import Chart
from app.automated_form import Form


class Executables():

    __run: bool
    __charts: Chart
    __form: Form

    def __init__(self) -> None:
        self.__run = True

    def menu_automated_charts(self) -> None:
        self.__import_settings(type = "charts")
        self.__charts = Chart()
        self.__menu(quantity_of_options = 5, type = "charts")
        

    def menu_automated_form(self) -> None: 
        self.__import_settings(type = "form")
        self.__form = Form()
        self.__menu(quantity_of_options = 2, type = "form")
    
    def __menu(self, quantity_of_options: int, type: str):
        self.__run = True
        while (self.__run):
            if type == "charts": self.__automated_charts_options()
            elif type == "form": self.__automated_form_options()
            option_selected = self.__read_option(default_option = quantity_of_options)
            self.__run = False if option_selected == quantity_of_options else True
            self.__execute_option(option_selected, type)

    def __read_option(self, default_option: int) -> int:
        try:
            option_selected = int(input("""
        Enter your option: """))
        except ValueError:
            print("""
            xxxxx Invalid option selected xxxxx
            """)
            option_selected = default_option
        return option_selected
    
    def __execute_option(self, option_selected: int, type: str) -> None:
        if type ==  "charts":
            if option_selected == 1:
                print("""
                Getting data ...""")
                self.__charts.get_data()
                data = self.__charts.raw_data()
                print("""
                ------ Data ------
                """)
                for i in data: 
                    print(i)
            elif option_selected == 2:
                data = self.__charts.raw_data()
                print("""
                ------ Data ------
                """)
                for i in data: 
                    print(i)
            elif option_selected == 3:
                print("""
                Chart created""")
                self.__charts.create_chart()
            elif option_selected == 4:
                self.__charts.create_file_csv()
                print("""
                CVS file created""")
            elif option_selected == 5:
                print("""
                        ooooo Exit ooooo
                """)
                self.__run = False
            else:
                print("""
                xxxxx That option dosen't exist xxxxx
                """)
                self.__run = False
        elif type == "form":
            if option_selected == 1:
                print("""
                Filling form ...""")
                self.__form.open()
                self.__form.fill_fields()
            elif option_selected == 2:
                print("""
                        ooooo Exit ooooo
                """)
                self.__run = False
            else:
                print("""
                xxxxx That option dosen't exist xxxxx
                """)
                self.__run = False
        else:
            print("""
            xxxxx That option dosen't exist xxxxx
            """)
            self.__run = False
        

    def __import_settings(self, type: str) -> None:
        try:
            answer = input("""Do you want to import the example configuration for this exercise? (y/n): """)
        except ValueError:
            answer = "y"
        if answer == "y":
            with open("source/assets/settings.json", "r") as jsonFile:
                data = json.load(jsonFile)
            if type == "charts":
                data["import_settings"] = "source/assets/examples/automated_chart_setup_example.json"
            elif type == "form":
                data["import_settings"] = "source/assets/examples/automated_form_setup_example.json"
            with open("source/assets/settings.json", "w") as jsonFile:
                json.dump(data, jsonFile)
        elif answer == "n":
            print("""
            ooooo No settings imported ooooo
            """)
            return
    

    def __automated_charts_options(self) -> None:
        print("""
            ooooo Automated charts exercise ooooo
            """)
        print("""
                ------ Options ------""")
        print("""
        1.- Get data from website
        2.- Show collected data
        3.- Create chart
        4.- Create csv file
        5.- Back to de main menu""")

    def __automated_form_options(self) -> None:
        print("""
            ooooo Automated form exercise ooooo
            """)
        print("""
                ------ Options ------""")
        print("""
        1.- Fill form
        2.- Back to de main menu""")