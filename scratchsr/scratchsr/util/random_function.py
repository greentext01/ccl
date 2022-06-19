from random import choice

from scratchsr.util.random_str import random_str

CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def random_function():
    return random_str(CHARS)
