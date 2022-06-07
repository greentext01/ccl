import random


def gen_id():
    characters = "!#%()*+,-./:;=?@[]^_`{|}~ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    out = ""
    
    for _ in range(20):
        out += random.choice(characters)
        
    return out
