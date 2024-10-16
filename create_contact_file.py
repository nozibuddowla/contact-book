def create_contact(contact_book):
    name = input('Enter name: ').strip()

    phone = input('Enter phone number: ').strip()
    
    email = input('Enter email: ').strip()

    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }

    contact_book.append(contact)

    print('contact created successfully!')

    return contact_book