def tiggerfy(s):
    result = ""
    for c in s:
        if c.lower() not in "tiger":
            result += c 
        return result
    