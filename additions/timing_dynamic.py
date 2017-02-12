
def eff_way(table):
    l = len(table)+1
    table_2 = [[0 for j in range(l)] for i in range(l)]
    for i in range(l-1):
        for j in range(l-1): 
            if i == 0 and j == 0:
                table_2[i+1][j+1] = table[i][j]
            elif i == 0:
                table_2[i+1][j+1] = table_2[i+1][j]+ table[i][j]
            elif j == 0:
                table_2[i+1][j+1] = table_2[i][j+1]+ table[i][j]
            else:
                table_2[i+1][j+1] = min(table_2[i+1][j], table_2[i][j+1]) + table[i][j]

    return table_2[l-1][l-1]


if __name__ == '__main__':
    import time
    import random
    import matplotlib.pyplot as plt

    table =[[1,2,3],[4,5,6],[7,8,9]]
    times=[]
    for i in range(200):
        start = time.time()
        eff_way(table)
        end = time.time()
        times.append(end - start)

        table.append(table[1])
        for j in table:
            j.append(random.randint(0,9))
    print(times)

    plt.plot(times)
    plt.ylabel('time')
    plt.xlabel('table size')
    plt.title('Run time dynamic programming')
    plt.savefig('plot2.png', format='png')

 
