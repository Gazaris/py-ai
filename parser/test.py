words = ['13', '1999', '2001', '280', 'aMazon1', 'aNotHer,', 'apRil', '.']

words = [w for w in words if any(c.isalpha() for c in w)]

words = [w.lower() for w in words]

print(words)