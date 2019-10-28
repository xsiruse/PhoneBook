# def referrer_func(referrer):
#     def ref_name():
#         referrer_func_name = referrer.__name__()
#         print(referrer_func_name)
#         referrer()
#     return ref_name()


class Contact:

    def __init__(self, lastname, firstname, phone, fav=False, *args, **kwargs):
        self.lastname = lastname
        self.firstname = firstname
        self.phone = phone
        self.fav = bool(fav)
        self.additional_info = [*args], {**kwargs}

    def __str__(self):
        add_inf = []
        for li in self.additional_info[0]:
            add_inf.append(li)
        for k, v in self.additional_info[1].items():
            add_inf.append(f'{k}: {v}')
        x = ('\n\t\t'.join(add_inf))
        return f'Имя: {self.firstname}\nФамилия: {self.lastname}\nТелефон: {self.phone}\nВ избранных: {self.fav}\n\
Дополнительная информация:\n\t\t{x}'


# jhon = Contact('Jhon', 'Smith', '+71234567809', True, 'dummy', 'farmer', telegram='@jhony', email='jhony@smith.com')


# print(jhon.additional_info)
# print(jhon.__str__())


class PhoneBook(list):

    def __init__(self, book_name):
        super().__init__()
        self.book_name = book_name

    def contacts_list(self):
        print(self)
        for contact in self:
            print(contact)

    def add_contact(self, *args):
        print(self)
        new_contact = Contact(*args)
        self.append(new_contact)
        print(self)

    def delete_contact(self, num):
        for d in self:
            if d.__dict__['phone'] == num:
                del d
                print('record deleted successfully')
            # elif d.__dict__['phone'] != num:
            #     pass
            # else:
            #     print('No such number')

    def find_favorite(self):
        for d in self:
            if d.__dict__['fav']:
                print(d)

    def find_contact(self, lastname, firstname):
        for d in self:
            if d.__dict__['lastname'] == lastname and d.__dict__['firstname'] == firstname:
                print(d)


# @referrer_func
def main():
    """
1 - Вывод контактов из телефонной книги;
2 - Добавление нового контакта;
3 - Удаление контакта по номеру телефона;
4 - Поиск всех избранных номеров;
5 - Поиск контакта по имени и фамилии.
      """

    try:

        print(main.__doc__)
        op = int(input('Please insert the command: '))
        if op == 1:
            new_book.contacts_list()
            main()
        elif op == 2:
            lastname = input('Please enter lastname: ')
            firstname = input('Please enter firstname: ')
            phone = str(input('Please enter phone: '))
            fav = input('Add to favorites? (0 no /1 yes): ')
            new_book.add_contact(lastname, firstname, phone, fav)
            main()
        elif op == 3:
            # print(new_book)
            if len(new_book) != 0:  # if not new_book not worked
                num = input('Please enter phone number: ')
                new_book.delete_contact(num)
                main()
            else:
                print('!!! Phone Book is empty yet! Please use command 2 to add contacts...')

        elif op == 4:
            new_book.find_favorite()
            main()
        elif op == 5:
            lastname = input('Please enter lastname: ')
            firstname = input('Please enter firstname: ')
            new_book.find_contact(lastname, firstname)
            main()
        else:
            raise ValueError

    except ValueError:
        print('Некорректный ввод, повторите еще раз')
        main()


if __name__ == "__main__":
    b_name = input('Please enter the book name: ')
    new_book = PhoneBook(b_name)
    main()
