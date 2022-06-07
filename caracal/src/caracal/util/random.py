from random import choice

CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def random():
    return "".join(choice(CHARS) for _ in range(41))
