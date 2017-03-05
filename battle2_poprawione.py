def battle(soldier_list):
    even = []
    odd = []

    for i in soldier_list:
        if i == 0:
            pass
        elif i%2 == 0:
            if i < 0:
                even.append(('min', bin(i)[3:].count('0')))
            else:
                even.append(('plus', bin(i)[2:].count('0')))
        else:
            if i < 0:
                odd.append(('min', bin(i)[3:].count('1')))
            else:
                odd.append(('plus', bin(i)[2:].count('1')))
    
    sum_even = summer(even)
    sum_odd = summer(odd)
    
    if sum_even > sum_odd:
        return 'evens win'
    elif sum_even < sum_odd:
        return 'odds win'
    else:
        return 'tie'   
  

def summer(list_numbers):
    ''' This function takes as argument list of tuples i.e. ('min', 7). 
        First element in tuple is a string which contains information, 
        whether the second element has to be added to result ('plus') or 
        subtracted from result ('min'). 
        Function returns sum of second elements of tuple with proper sign.
    ''' 

    result = 0
    for sign, number in list_numbers:
        if sign == 'min':
            result -= number
        else:
            result += number
    
    return result





if __name__ == '__main__':
#    a=[5, 3, 14,-16,0]
#    a=[5, 3, 14]
#    a=[21,-3,20]
#    a=[7,-3,-14,6]
#    a=[17,-3, 32, -24]

    a=[0,1,2]
    print (battle(a))






