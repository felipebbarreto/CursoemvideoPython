ex = str(input('Digite uma expressão matemática: '))
esq = dir = 0
for c in ex:
    if c == '(':
        esq += 1
    if c == ')':
        dir += 1
if esq == dir:
    print('\033[32mEssa expressão é válida!')
else:
    print('\033[31mEssa expressão é inválida!')
