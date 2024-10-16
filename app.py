contact_book = [
    {
        'name': 'Nozib',
        'phone': '01922438860',
        'email': 'nozibuddowla@gmail.com'
    }, 
    {
        'name': 'Niloy',
        'phone': '01781858209',
        'email': 'niloyfardinahmed@gmail.com'
    },
    {
        'name': 'Rafat',
        'phone': '01715226693',
        'email': 'sfkrafat3@gmail.com'
    },
    {
        'name': 'Jinat',
        'phone': '01643660509',
        'email': 'jinatsultana47@gmail.com'
    },
    
]

# contact_book = []

def create_contact():
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

def view_all_contact():
    for contact in contact_book:
        print(contact['name'], contact['phone'], contact['email'], sep='|')

def search_contacts():
    search_term = input('Enter what you want to search: ').strip()
    for contact in contact_book:
        if search_term.lower() in contact['name'].lower(): 
            print(f"Found: {contact['name']} - {contact['phone']}")

def remove_contact():
    search_term = input('Enter text to search: ').strip()
    for index, contact in enumerate(contact_book):
        if search_term.lower() in contact['name'].lower():
            print(f" {index+1}. {contact['name']} - {contact['phone']} ")
    selected_index = int(input('Enter an contact to remove: ').strip())
    contact_book.pop(selected_index - 1)
    print('Contact remove successfully!')

def update_contact():
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

print('Welcome!')
menu_text = """
Options:
1. Create Contact
2. View all Contacts
3. Search Contacts
4. Remove Contact
5. Update Contact
0. Exit
"""

while True:
    print(menu_text)
    choice = input('Enter you choice: ').strip()
    
    if choice == "1":
        create_contact()
    elif choice == '2':
        view_all_contact()
    elif choice == '3':
        search_contacts()
    elif choice == '4':
        remove_contact()
    elif choice == '5':
        update_contact()
    elif choice == '0':
        break
    else:
        print('Wrong Choice!')