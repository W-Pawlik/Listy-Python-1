

cytat = """
Magia jest w opinii niektórych ucieleśnieniem Chaosu. Jest kluczem zdolnym otworzyć
zakazane drzwi. Drzwi, za którymi czai się koszmar, zgroza i niewyobrażalna okropność,
za którymi czyhają wrogie, destrukcyjne siły, moce czystego zła, mogące unicestwić nie
tylko tego, kto drzwi te uchyli, ale i cały świat. A ponieważ nie brakuje takich, którzy przy
owych drzwiach manipulują, kiedyś ktoś popełni błąd, a wówczas zagłada świata będzie
przesądzona i nieuchronna. Magia jest zatem zemstą i orężem Chaosu. To, że po
Koniunkcji Sfer ludzie nauczyli posługiwać się magią, jest przekleństwem i zgubą świata.
Zgubą ludzkości. I tak jest. Ci, którzy uważają magię za Chaos, nie mylą się.
"""

cytat_lower = cytat.lower()
cytat_swapcase = cytat.swapcase()
cytat_capitalize = cytat.capitalize()
cytat_replace = cytat.replace("Magia", "Moc")
cytat_lstrip = cytat.lstrip()
cytat_rstrip = cytat.rstrip()
cytat_reversed = ''.join(reversed(cytat))
cytat_count_a = cytat.count('a')
cytat_find_Chaos = cytat.find('Chaos')
cytat_isalnum = cytat.isalnum()
cytat_startswith_Magia = cytat.startswith('Magia')
cytat_endswith_chaos = cytat.endswith('sie.\n')

print(f"Original:\n{cytat}\n")
print(f"Lower:\n{cytat_lower}\n")
print(f"Swapcase:\n{cytat_swapcase}\n")
print(f"Capitalize:\n{cytat_capitalize}\n")
print(f"Replace 'Magia' with 'Moc':\n{cytat_replace}\n")
print(f"Left strip:\n{cytat_lstrip}\n")
print(f"Right strip:\n{cytat_rstrip}\n")
print(f"Reversed:\n{cytat_reversed}\n")
print(f"Count 'a': {cytat_count_a}\n")
print(f"Find 'Chaos': {cytat_find_Chaos}\n")
print(f"Is alphanumeric: {cytat_isalnum}\n")
print(f"Starts with 'Magia': {cytat_startswith_Magia}\n")
print(f"Ends with 'się.\\n': {cytat_endswith_chaos}\n")
