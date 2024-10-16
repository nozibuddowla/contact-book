def search_contacts(contact_book):
    search_term = input('Enter what you want to search: ').strip()

    for contact in contact_book:
        if search_term.lower() in contact['name'].lower(): 
            print(f"Found: {contact['name']} - {contact['phone']}")