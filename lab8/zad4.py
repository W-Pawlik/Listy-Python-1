import json

serniczkowy_spam = {
    "1@gmail.com": True,
    "2@gmail.com": True,
    "3@gmail.com": True,
    "4@gmail.com": True
}

def export_to_json(spam_list, filename):
    with open(filename, "w") as f:
        json.dump(spam_list, f)

export_to_json(serniczkowy_spam, 'serniczkowy_spam.json')

def import_from_json(filename):
    with open(filename, "r") as f:
        return json.load(f)

print(f'Zaimporotwane dane: {import_from_json('serniczkowy_spam.json')}')
