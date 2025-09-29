# `pwdgen`

A secure password generator

```text
usage: pwdgen [-h] [-V] [-b] [--hex] [-d] [-l LENGTH]

A secure password generator

options:
  -h, --help           show this help message and exit
  -V, --version        show program's version number and exit
  -b, --base85         generate a base85 password
  --hex                generate a hex password
  -d, --digits         generate a password of digits
  -l, --length LENGTH  choose a password length (default: 32)
```

## Installation

### Prerequisites

- Python >= 3.6
- [pipx](https://pipx.pypa.io/stable/installation/#on-linux)

```sh
pipx install pwdgen-py
```

## Usage

```sh
pwdgen
```

## License

[GNU General Public License v3.0 or later](https://github.com/mentiferous/pwdgen/blob/main/LICENSE)
