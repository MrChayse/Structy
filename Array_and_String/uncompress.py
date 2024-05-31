def uncompress(s, i=0, output=""):
    # Base case: if we reach the end of the string, return the output
    if i >= len(s):
        return output

    # Extract number
    num = 0
    while i < len(s) and s[i].isdigit():
        num = num * 10 + int(s[i])
        i += 1

    # Extract character and append it num times to the output
    if i < len(s) and s[i].isalpha():
        output += s[i] * num
        i += 1

    # Recursive call
    return uncompress(s, i, output)