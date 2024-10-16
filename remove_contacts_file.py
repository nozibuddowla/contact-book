def remove_contact(contact_book):
    search_term = input('Enter text to search: ').strip()

    for index, contact in enumerate(contact_book):
        if search_term.lower() in contact['name'].lower():
            print(f" {index+1}. {contact['name']} - {contact['phone']} ")

    selected_index = int(input('Enter an contact to remove: ').strip())

    contact_book.pop(selected_index - 1)

    print('Contact remove successfully!')

    return contact_book