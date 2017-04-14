def show_primary_menu():
    print('\nPlease choose your action:')
    print('1) Create new record\n', '2) View/Edit existing record\n', '3) Exit\n', sep='')


def show_secondary_menu():
    print('\nPlease choose your action:')
    print('1) Read existing record\n', '2) Update existing record\n', '3) Delete existing record\n', '4) Exit\n', sep='')


def create_new_contact():
    new_contact = []
    new_contact.append(input('\nNew contact name: '))
    new_contact.append(input('New contact number: '))
    return new_contact


def find_contact():
    pass


def get_action():
    action = input('Selection: ')
    return action


def print_error():
    print('\n[FAIL] Breaking rules will get you nowhere >:D')

