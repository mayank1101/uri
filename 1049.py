w1 = raw_input()
w2 = raw_input()
w3 = raw_input()
if w1 == 'vertebrado':
    if w2 == 'ave':
        if w3 == 'carnivoro':
            print ('aguia')
        elif w3 == 'onivoro':
            print ('pomba')
    elif w2 == 'mamifero':
        if w3 == 'onivoro':
            print ('homem')
        elif w3 == 'herbivoro':
            print ('vaca')
elif w1 == 'invertebrado':
    if w2 == 'inseto':
        if w3 == 'hematofago':
            print ('pulga')
        elif w3 == 'herbivoro':
            print ('lagarta')
    elif w2 == 'anelideo':
        if w3 == 'hematofago':
            print ('sanguessuga')
        elif w3 == 'onivoro':
            print ('minhoca')