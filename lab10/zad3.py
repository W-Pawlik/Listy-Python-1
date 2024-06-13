
text = "Długo na szturm i szaniec poglądał w milczeniu. Na koniec rzekł: 'Stracona'."

first_period_index = text.find('.')

if first_period_index != -1:
    result = text[:first_period_index + 1]
else:
    result = text 

print(f"Wycinek: {result}")

words = ["Zwinny", "lis", "przeskoczył", "nad", "leniwym", "psem", "."]

sentence = ' '.join(words[:-1]) + words[-1]
print(f"Zdanie: {sentence}")
