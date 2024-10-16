def restore_contact(contact_book):
    
    contact_book.clear()

    with open('contacts.csv', 'r') as file_pointer:
        for line in file_pointer.readlines():
            line_splitted = line.strip().split(',')

            contact = {
                'name': line_splitted[0],
                'phone': line_splitted[1],
                'email': line_splitted[2],
            }

            contact_book.append(contact)

    print('Contacts Restored!')

    return contact_book