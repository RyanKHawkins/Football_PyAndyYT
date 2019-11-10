# Name:  helpers.py


def select_from_menu(menu_dict: dict):
    selection = input('Make selection: ')
    # do some dodgy things :)
    action = menu_dict.get(int(selection), None)
    if action is None:
        print('Invalid selection')
    else:
        print()
        action()
        print()
