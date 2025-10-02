# SPDX-License-Identifier: GPL-3.0-or-later
#
# pwdgen - A secure password generator
# Copyright (C) 2025 mentiferous
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>

"""cli.py - Main module for pwdgen."""

import argparse

from pwdgen import __version__
from pwdgen.gen.pwd import gen_base85, gen_digits, gen_hex
from pwdgen.helper import pwd_table


def main():
    parser = argparse.ArgumentParser(
        prog="pwdgen",
        description="A secure password generator",
    )

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
        help="generate a base85 password",
    )
    parser.add_argument(
        "--hex",
        action="store_true",
        help="generate a hex password",
    )
    parser.add_argument(
        "-d",
        "--digits",
        action="store_true",
        help="generate a password of digits",
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
        pwd_table("base85", gen_base85(args.length), args.length)

    elif args.hex:
        pwd_table("hex", gen_hex(args.length), args.length)

    elif args.digits:
        pwd_table("digits", gen_digits(args.length), args.length)

    else:
        parser.print_help()
