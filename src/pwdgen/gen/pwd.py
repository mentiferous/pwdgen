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

"""pwd.py - Module for generating passwords."""

from base64 import b85encode
from secrets import choice, token_bytes, token_hex
from string import digits


def gen_base85(length):
    """Generate a base85 password."""

    return b85encode(token_bytes(length)).decode()[:length]


def gen_hex(length):
    """Generate a hex password."""

    return token_hex(length)[:length]


def gen_digits(length):
    """Generate a password of digits."""

    return "".join(choice(digits) for _ in range(length))
