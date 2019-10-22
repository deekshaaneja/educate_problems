import copy

def permute(data,i,length):
    if i==length: 
        print(''.join(data) )
    else:
        for j in range(i,length): 
            #swap
            data[i], data[j] = data[j], data[i] 
            permute(data, i+1, length) 
            data[i], data[j] = data[j], data[i]



print(permute(['a','b'],0,2))


