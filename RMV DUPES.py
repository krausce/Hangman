def removeDuplicate(s):
    c = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for i in s:
        if i in c:
         result += i
        elif i not in c:
            result += ''
            return ''.join(result)

    return sorted(result.replace(" ",""))
s = 'abcdefasdlkfjc goiesla;'
print(removeDuplicate(s))