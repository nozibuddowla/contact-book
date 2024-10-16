import create_contact_file
import view_all_contacts_file
import search_contacts_file
import remove_contacts_file
import update_contact_file
import backup_contact_file
import restore_contact_file

contact_book = []

print('Welcome!')

menu_text = """
Options:
1. Create Contact
2. View all Contacts
3. Search Contacts
4. Remove Contact
5. Update Contact
6. Backup Contact
7. Restore Contact
0. Exit
"""

while True:
    print(menu_text)
    
    choice = input('Enter you choice: ').strip()
    
    if choice == "1":
        contact_book = create_contact_file.create_contact(contact_book)
    elif choice == '2':
        view_all_contacts_file.view_all_contact(contact_book)
    elif choice == '3':
        search_contacts_file.search_contacts(contact_book)
    elif choice == '4':
        contact_book = remove_contacts_file.remove_contact(contact_book)
    elif choice == '5':
        contact_book = update_contact_file.update_contact(contact_book)
    elif choice == '6':
        contact_book = backup_contact_file.backup_contact(contact_book)
    elif choice == '7':
        contact_book = restore_contact_file.restore_contact(contact_book)
    elif choice == '0':
        break
    else:
        print('Wrong Choice!')