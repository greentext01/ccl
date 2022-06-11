from random import choice


def random_str(chars, len=20):
    return "".join(choice(chars) for _ in range(len))
