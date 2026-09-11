contacts = [
    {'name': 'Analo Brian', 'phone': '0712345671', 'skill': 'driver', 'city': 'Kakamega'},
    {'name': 'Millicent Kay', 'phone': '0798765432', 'skill': 'teacher', 'city': 'Eldoret'},
    {'name': 'Ian Mburu', 'phone': '0712398751', 'skill': 'painter', 'city': 'Bungoma'},
    {'name': 'Emmanuel Tei', 'phone': '0798761568', 'skill': 'chef', 'city': 'Nairobi'},
    {'name': 'Patrick Shakes', 'phone': '0743129867', 'skill': 'tailor', 'city': 'Nakuru'},
]
print('Before:', len(contacts), 'contacts')
print('==== CONTACT BOOK ====')
for i, contact in enumerate(contacts):
   print(f'\n{i+1}. {contact['name']}')
   print(f'  Phone : {contact['phone']}')
   print(f'  Skill : {contact['skill']}')
   print(f'  City : {contact['city']} ')

# Search by name and print the result
search_name = 'Patrick Shakes'
found = False
for contact in contacts:
    if contact['name'] == search_name:
        print('Contact found')
        print(f' Name: {contact['name']}')
        print(f' Phone: {contact['phone']}')
        print(f' Skill: {contact['skill']}')
        print(f' City: {contact['city']}')
        found = True
        break
if not found:
    print('Contact not found:', search_name)

# Search by city
search_city = 'Eldoret'
print(f'contacts in {search_city}:')
for contact in contacts:
    if contact['city'] == search_city:
         print(f'{contact['name']} | {contact['phone']} | {contact['skill']}')

# Adding a new contact
new_contact = [
{'name' : 'Juma John', 
'phone': '0786431270', 
'skill' : 'plumber', 
'city' : 'Naivasha'}
]
contacts.append(new_contact)
print('After:', len(contacts), 'contacts')
print('Last contact:', contacts[-1])