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
    import time
    import random
    import matplotlib.pyplot as plt

    times=[]
    for i in range(11):
        start = time.time()
        search(0, 0)
        end = time.time()
        times.append(end - start)
        
        table.append(table[1])
        for j in table:
            j.append(random.randint(0,9))
    print(times)

    plt.plot(times)
    plt.ylabel('time')
    plt.xlabel('table size')
    plt.title('Run time recursion')
    plt.savefig('plot1.png', format='png')




