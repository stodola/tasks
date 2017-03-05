def battle(soldier_list):
    sum_even = 0
    sum_odd = 0

    for i in soldier_list:
        if i == 0:
            pass
        elif i%2 == 0:
            if i < 0:
                sum_even -=  bin(i)[3:].count('0')
            else:
                sum_even += bin(i)[2:].count('0')
        else:
            if i < 0:
                sum_odd -= bin(i)[3:].count('1')
            else:
                sum_odd += bin(i)[2:].count('1')
    
    
    if sum_even > sum_odd:
        return 'evens win'
    elif sum_even < sum_odd:
        return 'odds win'
    else:
        return 'tie'   
  



if __name__ == '__main__':
#    a=[5, 3, 14,-16,0]
#    a=[5, 3, 14]
#    a=[21,-3,20]
#    a=[7,-3,-14,6]
#    a=[17,-3, 32, -24]

    a=[0,1]
    print (battle(a))






