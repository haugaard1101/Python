directors = {'Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren'}
management = {'Tine', 'Trunte', 'Rane'}
employees = {'Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent', 'Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars'}

svar1 = directors - employees
print(svar1)

svar2 = directors & employees
print(svar2)

svar3 = len(management & directors)
print(svar3)

svar4 = management <= employees
print(svar4)

svar5 = management <= directors
print(svar5)

svar6 = directors & employees & management
print(svar6)

svar7 = employees - directors - management
print(svar7)