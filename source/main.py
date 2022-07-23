from classes.browser import Browser

def main():
    b = Browser()
    b.open()
    b.find_elements()
    data = b.get_data_elements()
    print(data[0])
    b.close()

if __name__ == "__main__":
    main()
