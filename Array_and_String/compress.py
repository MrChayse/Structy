def compress(s, i = 0, j = 1, output = []):
    if i == len(s): return ''.join(output)

    count = 1
    while j < len(s) and s[j] == s[i]:
        j += 1
        count += 1

        
    output.append(f"{count}{s[i]}") if count > 1 else output.append(s[i])

    return compress(s, j, j + 1, output)

#print(compress('ccaaatsss'))
#print(compress('ssssbbz'))
#print(compress('ppoppppp'))
#print(compress('nnneeeeeeeeeeeezz'))
print(compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'))
    