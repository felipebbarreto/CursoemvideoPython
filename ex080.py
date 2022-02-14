lista = [1]
for c in range(1,6):
    n = int(input('Digite um valor: '))
    if n > lista[-1]:
        lista.append(n)
    else:
        for pos,num in enumerate(lista):
            if n <= num:
                lista.insert(pos,n)
                break
lista.remove(1)
print(lista)
