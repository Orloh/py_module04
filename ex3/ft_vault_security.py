# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_vault_security.py                              :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: orhernan <ohercelli@gmail.com>            +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/03/28 23:46:52 by orhernan         #+#    #+#              #
#    Updated: 2026/03/29 00:52:04 by orhernan        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


def secure_vault_ops(filename: str, messages: list[str]) -> None:
    """
    Securely reads a storage vault and appends classified data.
    Aborts if vault is missing.
    """
    print()
    print("Initiating secure vault access")
    missing_newline = False

    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            print("Vault connection established with failsafe protocols")
            print()
            print("SECURE EXTRACTION:")

            for line in file.readlines():
                print(f"[CLASSIFIED] {line.rstrip()}")
                missing_newline = not line.endswith("\n")
            print()

    except FileNotFoundError:
        print(f"ERROR: Vault '{filename}' not found in the storage matrix.")
        print("Operation aborted. Vault automatically sealed for safety.")
        return

    with open(filename, mode="a", encoding="utf-8") as file:
        print("SECURE PRESERVATION:")

        if missing_newline:
            file.write("\n")

        for message in messages:
            entry = f"[CLASSIFIED] {message}\n"
            file.write(entry)
            print(entry.rstrip())
        print()
    print("Vault automatically sealed upon completion")
    print()
    print("All vault operations completed with maximum security.")


def main() -> None:
    """
    Main entry point for testing Vault Security protocols.
    """
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM")

    vault_name = "classified_data.txt"
    messages: list[str] = [
        "New security protocols archived"
    ]

    secure_vault_ops(vault_name, messages)


if __name__ == "__main__":
    main()
