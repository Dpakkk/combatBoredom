# O(n)
string = 'I love New York'

def characterCount(string):
    # char extraction
    string = string.replace(" ","").lower()
    ch = []
    for i in string:
        ch.append(i)
    # duplication
    duplicate = []
    arr_sort = sorted(ch)
    for i in range(len(arr_sort) - 1):
        if arr_sort[i] == arr_sort[i-1]:
            duplicate.append(arr_sort[i])
    return duplicate
    
print("Duplicate character's are: {}".format(characterCount(string)))