

def palindromeChecker(s, startIndex, endIndex, subs):
    queries = [[startIndex[i], endIndex[i], subs[i]] for i in range(len(subs))]
    letter_occurrences = [0] * 26
    bit_values = []
    bit_value = 1
    odd_value = 0
    odd_values = []
    ret = []
    
    
    for i in range(31):
        bit_values.append(bit_value)
        bit_value *= 2
        
    
    for letter in s:
        index = ord(letter) - 97
        letter_occurrences[index] += 1
        odd_value += bit_values[index] if (letter_occurrences[index] & 1) else -bit_values[index]
        odd_values.append(odd_value)
        
        
    for query in queries:
        length = query[1] - query[0] + 1
        
        
        if (length <= 2 * query[2]):
            ret.append(True)
        else:
            odd_value = odd_values[query[1]] ^ odd_values[query[0] - 1] if query[0] > 0 else odd_values[query[1]]
            odds = bin(odd_value).count("1") - 1 if length & 1 else bin(odd_value).count("1")

            
            if (odds % 2 == 0 and odds // 2 <= query[2]):
                ret.append(True)
            else:
                ret.append(False)
                
    return ret