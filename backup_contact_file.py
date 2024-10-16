def backup_contact(contact_book):

    with open('contacts.csv', 'wt') as file_pointer:

        for contact in contact_book:
            line = f"{contact['name']},{contact['phone']},{contact['email']}\n"

            file_pointer.write(line)
    
    print('contacts backed up!')

    return contact_book