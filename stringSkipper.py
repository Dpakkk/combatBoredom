string = 'kathmandu'
skipperLength = 3

def skipperString(string, skipperLength):
    output = ''
    for i in range(len(string))[::skipperLength]:
        output += string[i]
    return output
    
print(skipperString(string,skipperLength))s