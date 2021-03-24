import pickle

class CellPhone:

    def __init__(self, manufact, model, price):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = price


    def set_manufact(self, manufact):
        self.__manufact = manufact
    

    def set_model(self, model):
        self.__model = model


    def set_retail_price(self, price):
        self.__retail_price = price


    def get_manufact(self):
        return self.__manufact


    def get_model(self):
        return self.__model


    def get_retail_price(self):
        return self.__retail_price


def main():
    make_list()
    unpickle_cellphone()
    #display_list(phones)


def make_list():
    #phone_list = []
    print('Give the data for 5 Cellphones.')
    print('')
    with open(r'C:\Users\bilakos\Desktop\PYTHON_PROJECTS\PYTHON_TEST\cellphone.dat', 'wb') as cp_f:
        for count in range(1, 4):
            print(f'Cellphone no.{count}:')
            print('')    
            mn = input('Give the brand: ')
            md = input('Give the model number: ')
            retail = float(input('Give the retail price: '))
            print()

            phone = CellPhone(mn, md, retail)
            #phone_list.append(phone)
            pickle.dump(phone, cp_f)
    #return phone_list


def unpickle_cellphone():
    end_of_file = False
    with open(r'C:\Users\bilakos\Desktop\PYTHON_PROJECTS\PYTHON_TEST\cellphone.dat', 'rb') as cp_f:
        while not end_of_file:
            try:
                phone = pickle.load(cp_f)
                display_data(phone)
            except Exception:
                end_of_file = True


def display_data(phone):
    print('Brand: ', phone.get_manufact())
    print('Model Number: ', phone.get_model())
    print('Retail Price: %.2f€'%(phone.get_retail_price()))
    print()


def display_list(phones):
    for item in phones:
        print('The data you give is the ones below:\n')
        print(f'Brand: {item.get_manufact()}')
        print(f'Model: {item.get_model()}')
        print('Retail Price: €%.2f'%(item.get_retail_price()))
        print()


main()