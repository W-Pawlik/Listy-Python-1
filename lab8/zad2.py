
contacts = {
    "Jan Kowalski": "123-456-789",
    "Anna Nowak": "987-654-321",
    "Piotr Zieliński": "234-567-890",
    "Maria Wiśniewska": "345-678-901",
    "Krzysztof Wójcik": "456-789-012",
    "Agnieszka Krawczyk": "567-890-123",
    "Tomasz Lewandowski": "678-901-234",
    "Ewa Kamińska": "789-012-345",
    "Marek Piotrowski": "890-123-456",
    "Magdalena Nowicka": "901-234-567"
}

contacts["Jan Kowalski"] = "Jan Plech"
contacts["Magdalena Nowicka"] = "Magdalena Skowron"

keys_to_remove = list(contacts.keys())[4:7]
for key in keys_to_remove:
    del contacts[key]

print("Lista kontaktow:")
for name, number in contacts.items():
    print(f"{name}: {number}")

contacts.clear()
contacts["Zofia Nowak"] = "111-222-333"
contacts["Adam Malinowski"] = "444-555-666"

print("\nLista kontaktow po dodaniu nowych pozycji:")
for name, number in contacts.items():
    print(f"{name}: {number}")

sorted_contacts = dict(sorted(contacts.items()))

print("\nPosortowana lista kontaktów:")
for name, number in sorted_contacts.items():
    print(f"{name}: {number}")

contacts_list = list(contacts.items())
sorted_contacts_list = sorted(contacts_list)

print("\nLista kontaktów jako posortowana lista:")
for name, number in sorted_contacts_list:
    print(f"{name}: {number}")
