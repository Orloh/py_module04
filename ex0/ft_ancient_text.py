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

def recover_vault_data(vault_name: str) -> str | None:
    """
    Attempts to open, read, and safely close the specified storage vault.
    Returns the recovered text, or None if the vault is missing.
    """

    try:
        vault = open(vault_name, "r")
        print("Connection established...")
        print()
        data: str = vault.read()
        vault.close()
        return data

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
        return None


def display_data(data: str) -> None:
    """
    Handles the presentation of the recovered archival data.
    """
    print("RECOVERED DATA:")
    print(data.strip())
    print()


def main() -> None:
    """
    Main entry point for the Data Recovery System.
    """
    vault_name = "ancient_fragment.txt"
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    print(f"Accessing Storage Vault: {vault_name}")
    recovered_text: str | None = recover_vault_data("ancient_fragment.txt")
    if recovered_text:
        display_data(recovered_text)
        print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
