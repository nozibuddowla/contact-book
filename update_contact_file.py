def update_contact(contact_book):
    found_search_result = False
    search_term = input('Enter text to search to update: ').strip()

    for index, contact in enumerate(contact_book):
        if search_term.lower() in contact['name'].lower():
            found_search_result = True
            print(f'{index + 1}. {contact['name']} - {contact['phone']}')

    if not found_search_result:
        print('No Item found')
        return
    
    selected_index = int(input('Enter an contact to update: ').strip())

    new_name = input('Enter new name: ').strip()
    new_phone = input('Enter new phone number: ').strip()
    new_email = input('Enter new email: ').strip()
        
    contact_book[selected_index - 1].update({
        'name': new_name,
        'phone': new_phone,
        'email': new_email,
    })
    print('Contact updated successfully!')

    return contact_book