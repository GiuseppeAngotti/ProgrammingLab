def sum_list(my_list):
    sum=0
    if(len(my_list)==0):
        return None
    for item in my_list:
        sum+=item
    return sum

list=[2,3,5]

risultato=sum_list(list)

print('La somma degli elementi è uguale a: {}'.format(risultato))