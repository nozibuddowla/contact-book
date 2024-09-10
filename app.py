# contact_book = [
#     {
#         'name': 'Nozib',
#         'phone': '01922438860',
#         'email': 'nozibuddowla@gmail.com'
#     }, 
#     {
#         'name': 'Niloy',
#         'phone': '01781858209',
#         'email': 'niloyfardinahmed@gmail.com'
#     },
#     {
#         'name': 'Rafat',
#         'phone': '01715226693',
#         'email': 'sfkrafat3@gmail.com'
#     },
# ]
contact_book = []

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

create_contact()
create_contact()

print(contact_book)