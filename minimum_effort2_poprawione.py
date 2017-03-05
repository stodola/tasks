import sys

def opener(path=None):
    if path:
        path = path
    else:
        path = sys.argv[1]
   
   with open(path) as file:
        while True:
            size = file.readline().rstrip()
            if size == '':
                break
            size_int =int(size)

            table =[]
            while size_int:
                table.append([int(i) for i in file.readline().rstrip().split(',')])
                size_int -= 1

            print (eff_way(table))


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
    
    opener()
    
