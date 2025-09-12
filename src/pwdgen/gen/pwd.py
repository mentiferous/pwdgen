from base64 import b85encode
from secrets import choice, token_bytes, token_hex
from string import digits


def gen_base85(length):
    """Generate a random base85 string."""

    return b85encode(token_bytes(length)).decode()[:length]


def gen_hex(length):
    """Generate a random hex string."""

    return token_hex(length)[:length]


def gen_digits(length):
    """Generate a random string of digits."""

    return "".join(choice(digits) for _ in range(length))
