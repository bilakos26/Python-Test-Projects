def main():
    n = eisagogi_n()
    emfanisi_max(n)

def eisagogi_n():
    n = int(input('Δώσε έναν αριθμό από το 1 έως το 9: '))
    return n

def emfanisi_max(n):
    lista = [1,2,3,4,5,6,7,8,9]
    for i in lista:
        if n < i:
            print(i)

main()