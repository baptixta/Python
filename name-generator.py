import random

# Arrays of names
name = ['João', 'Davi', 'Paulo', 'Gabriela', 'Rafaela', 'Joana', 'Kleber', 'Silvana', 'Denis', 'Maria']
lastName = ['Silva', 'Pereira', 'Rocha', 'Pinto', 'Santos', 'Chuasneguer', 'Pepino', 'Jorgeras', 'Zopede']

# Name Generator Function
def nameGenerator():
    nameRandom = random.choice(name) + ' '

    for lastname in range(0,2):
        lastNameRandom = random.choice(lastName)
        nameRandom +=  lastNameRandom + ' ' 

    return nameRandom

print(nameGenerator())
    
    