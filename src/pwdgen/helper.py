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

from rich.console import Console
from rich.table import Table


def pwd_table(name, password, length):
    table = Table()

    table.add_column(name, justify="center")
    table.add_column("length", justify="center")

    table.add_row(password, str(length))

    console = Console()

    console.print(table)
