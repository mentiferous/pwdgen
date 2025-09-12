import argparse

from pwdgen import __version__
from pwdgen.gen.pwd import gen_base85, gen_digits, gen_hex


def main():
    parser = argparse.ArgumentParser(prog="pwdgen")

    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=__version__,
    )
    parser.add_argument(
        "-b",
        "--base85",
        action="store_true",
        help="generate a random base85 password",
    )
    parser.add_argument(
        "--hex",
        action="store_true",
        help="generate a random hex password",
    )
    parser.add_argument(
        "-d",
        "--digits",
        action="store_true",
        help="",
    )
    parser.add_argument(
        "-l",
        "--length",
        default=32,
        type=int,
        help="choose a password length (default: 32)",
    )

    args = parser.parse_args()

    args.length = max(1, args.length)

    if args.base85:
        print(gen_base85(args.length))
    elif args.hex:
        print(gen_hex(args.length))
    elif args.digits:
        print(gen_digits(args.length))
    else:
        parser.print_help()
