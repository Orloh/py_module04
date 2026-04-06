# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_ancient_text.py                                :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/03/23 20:46:45 by orhernan         #+#    #+#              #
#    Updated: 2026/03/25 21:49:43 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    file_name = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")

    try:
        vault: typing.IO[str] = open(file_name, "r")

        data: str = vault.read()

        print("---")
        print()
        print(data, end="")
        if data and not data.endswith('\n'):
            print()
        print()
        print("---")

        vault.close()
        print(f"File '{file_name}' closed.")

    except OSError as e:
        print(f"Error opening file '{file_name}': {e}")


if __name__ == "__main__":
    main()
