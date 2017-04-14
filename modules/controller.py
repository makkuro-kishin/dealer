try:
    import configparser
    import modules.storage
    import modules.interaction
except Exception as import_error:
    print('[FAIL] Unable to import modules!\n', import_error, '\nAborting...', sep='')
    raise SystemExit


def get_primary_selection():
    modules.interaction.show_primary_menu()
    primary_action = modules.interaction.get_action()
    if primary_action == '1':
        contacts_list = {}
        new_contact = modules.interaction.create_new_contact()
        contacts_list.update({new_contact[0] : new_contact[1]})
        print('\nAdded new contact:', contacts_list)
        get_primary_selection()
    elif primary_action == '2':
        get_secondary_selection()
    elif primary_action == '3':
        raise SystemExit
    else:
        modules.interaction.print_error()
        get_primary_selection()


def get_secondary_selection():
    modules.interaction.show_secondary_menu()
    secondary_action = modules.interaction.get_action()
    if secondary_action == '1':
        print('TODO')
    elif secondary_action == '2':
        print('TODO')
    elif secondary_action == '3':
        print('TODO')
    elif secondary_action == '4':
        raise SystemExit
    else:
        modules.interaction.print_error()
        get_secondary_selection()


def controls():
    get_primary_selection()

