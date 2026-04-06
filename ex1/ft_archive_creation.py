# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_archive_creation.py                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/03/25 22:19:52 by orhernan         #+#    #+#              #
#    Updated: 2026/03/26 00:45:54 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


import sys
import typing


def print_data(data: str) -> None:
    print("---")
    print()

    print(data, end="")
    if data and not data.endswith('\n'):
        print()

    print()
    print("___")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 ft_archive_creation.py <file>")
        return

    file_name = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")

    try:
        vault: typing.IO[str] = open(file_name, "r")
        data: str = vault.read()
        print_data(data)
        vault.close()
        print(f"File '{file_name}' closed.")
        print()

    except OSError as e:
        print(f"Error opening file '{file_name}': {e}")
        return

    print("Transform data:")

    transformed_lines = [line + "#" for line in data.splitlines()]
    transformed_data = "\n".join(transformed_lines)

    print(transformed_data)

    new_file_name = input("Enter new file name (or empty): ")

    if not new_file_name:
        print("Not saving data.")
    else:
        print(f"Saving data to '{new_file_name}'")
        try:
            out_vault: typing.IO[str] = open(new_file_name, "w")

            out_vault.write(transformed_data + "\n")
            out_vault.close()

            print(f"Data saved in file '{new_file_name}'.")
        except OSError as e:
            print(f"Error opening file '{new_file_name}': {e}")


if __name__ == "__main__":
    main()
