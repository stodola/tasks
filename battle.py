def battle(soldier_list):
    even = []
    odd = []

    for i in soldier_list:
        if i == 0:
            pass
        elif i%2 == 0:
            if i < 0:
                even.append(('min', outcome_even(bin(i)[3:])))
            else:
                even.append(('plus', outcome_even(bin(i)[2:])))
        else:
            if i < 0:
                odd.append(('min', outcome_odd(bin(i)[3:])))
            else:
                odd.append(('plus', outcome_odd(bin(i)[2:])))
    
    sum_even = summer(even)
    sum_odd = summer(odd)
    
    if sum_even > sum_odd:
        return 'evens win'
    elif sum_even < sum_odd:
        return 'odds win'
    else:
        return 'tie'   
  

def summer(list_numbers):
    ''' This function takes as argument list of tuples i.e. ('min', 7). First element in tuple is a string which contains information, whether the second element has to be added to result ('plus') or subtracted from result ('min'). Function returns sum of second elements of tuple with proper sign.''' 

    result = 0
    for sign, number in list_numbers:
        if sign == 'min':
            result -= number
        else:
            result += number
    
    return result


def outcome_even(binary_num):
    '''This function takes as an argument binary number and returns number of zeros.'''
    
    outcome = 0
    for i in binary_num:
        if int(i) == 0:
            outcome += 1
    return outcome


def outcome_odd(binary_num):
    '''This function takes as an argument binary number and returns number of ones.'''
    
    outcome = 0
    for i in binary_num:
        if int(i) == 1:
            outcome += 1
    return outcome


if __name__ == '__main__':
    a=[5, 3, 14,-16,0]
    a=[5, 3, 14]
    a=[21,-3,20]
    a=[7,-3,-14,6]
    a=[17,-3, 32, -24]

#    a=[0,1]
    print (battle(a))






