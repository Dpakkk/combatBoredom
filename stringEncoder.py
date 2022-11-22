
def encondeMessage(s, sf):
    result = ''
    for i in range(len(s)):
        result += chr(ord(s[i])+1)
    return result
        
string = "Check1"
shift = 1

print(encondeMessage(string, shift))