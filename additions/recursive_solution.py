table =[[1,2,3],[4,5,6],[7,8,9]]

wynik = []

def search(x, y, suma =table[0][0]):

    if x == len(table)-1 and  y == len(table)-1:
        return wynik.append(suma)

    if x < len(table)-1:
        search(x+1, y, suma=suma +table[x+1][y])
    if y < len(table)-1:
        search(x, y+1, suma = suma +table[x][y+1])


if __name__ =='__main__':
    search(0, 0)

    print(min(wynik))

