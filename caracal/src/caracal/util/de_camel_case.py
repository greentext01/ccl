def de_camel_case(string: str):
    out = ""
    
    out += string[0].upper()
    for char in string[1:]:
        if char.isupper():
            out += " "
            out += char.lower()
        else:
            out += char
    
    return out
